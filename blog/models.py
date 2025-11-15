from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import math

class Category(models.Model):
    """
    Categories help organize blog posts by topic
    For example: Technology, Lifestyle, Travel, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})
    
    def post_count(self):
        # Returns number of published posts in this category
        return self.posts.filter(status='published').count()

class Tag(models.Model):
    """
    Tags are keywords that help readers find related content
    Multiple tags can be added to each post
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Main blog post model - stores all article data
    Each post has an author, category, tags, and content
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    # Basic post information
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    
    # Post content
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True, help_text="Short description for preview")
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    
    # Status and timestamps
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    # Engagement metrics - track views and likes
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Automatically set published date when post goes live
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
    
    def reading_time(self):
        # Calculate reading time based on average reading speed (200 words/min)
        word_count = len(self.content.split())
        minutes = math.ceil(word_count / 200)
        return minutes if minutes > 0 else 1
    
    def total_likes(self):
        # Count how many users liked this post
        return self.likes.count()
    
    def is_liked_by(self, user):
        # Check if a specific user has liked this post
        if user.is_authenticated:
            return self.likes.filter(id=user.id).exists()
        return False

class Comment(models.Model):
    """
    Comments allow readers to engage with posts
    Each comment is linked to a post and a user
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    # For nested replies (optional - can be added later)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
