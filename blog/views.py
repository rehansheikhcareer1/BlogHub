from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse
from .models import Post, Category, Tag, Comment
from .forms import PostForm, CommentForm

def home(request):
    """
    Homepage - shows all published posts with search and pagination
    Users can browse latest articles here
    """
    posts_list = Post.objects.filter(status='published')
    
    # Search feature - looks in title, content, and tags
    search_query = request.GET.get('search', '')
    if search_query:
        posts_list = posts_list.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()
    
    # Show 6 posts per page for better UX
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    # Get all categories for the filter section
    categories = Category.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
        'search_query': search_query,
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    """
    Shows full post content with comments and related articles
    Also tracks view count for analytics
    """
    post = get_object_or_404(Post, slug=slug, status='published')
    
    # Increment view count each time someone opens the post
    post.views += 1
    post.save(update_fields=['views'])
    
    # Get related posts from same category (max 3)
    related_posts = Post.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id)[:3]
    
    # Get all comments for this post
    comments = post.comments.all()
    
    # Comment form for logged in users
    comment_form = CommentForm()
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)

def explore(request):
    """
    Explore page - shows trending and popular content
    Helps users discover new articles
    """
    # Get trending posts (most views in last 30 days)
    trending_posts = Post.objects.filter(
        status='published'
    ).order_by('-views', '-published_at')[:6]
    
    # Get most liked posts
    popular_posts = Post.objects.filter(
        status='published'
    ).annotate(
        like_count=Count('likes')
    ).order_by('-like_count', '-published_at')[:6]
    
    # Get all categories with post counts
    categories = Category.objects.all()
    
    context = {
        'trending_posts': trending_posts,
        'popular_posts': popular_posts,
        'categories': categories,
    }
    return render(request, 'blog/explore.html', context)

def category_posts(request, slug):
    """
    Shows all posts from a specific category
    Helps users find content by topic
    """
    category = get_object_or_404(Category, slug=slug)
    posts_list = Post.objects.filter(category=category, status='published')
    
    # Pagination for better performance
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category_posts.html', context)

@login_required
def post_create(request):
    """
    Create new blog post - only for logged in users
    Author is automatically set to current user
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                form.save_m2m()  # Save tags (many-to-many field)
                messages.success(request, f'🎉 Post "{post.title}" created successfully!')
                return redirect('blog:post_detail', slug=post.slug)
            except Exception as e:
                messages.error(request, f'Error creating post: {str(e)}')
        else:
            messages.error(request, 'Please fix the errors in the form below.')
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})

@login_required
def post_update(request, slug):
    """
    Edit existing post - only the author can edit their own posts
    Security check ensures users can't edit others' content
    """
    post = get_object_or_404(Post, slug=slug)
    
    # Security: Check if current user is the post author
    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('blog:post_detail', slug=post.slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Update', 'post': post})

@login_required
def post_delete(request, slug):
    """
    Delete post - only author can delete
    Shows confirmation page before deleting
    """
    post = get_object_or_404(Post, slug=slug)
    
    # Security: Only author can delete their post
    if post.author != request.user:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('blog:post_detail', slug=post.slug)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('blog:home')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

@login_required
def my_posts(request):
    """
    Dashboard showing all posts by current user
    Includes both drafts and published posts
    """
    posts_list = Post.objects.filter(author=request.user)
    
    # Show 10 posts per page in dashboard
    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
    }
    return render(request, 'blog/my_posts.html', context)

@login_required
def post_like(request, slug):
    """
    Like/Unlike a post - AJAX endpoint
    Toggles like status for the current user
    """
    post = get_object_or_404(Post, slug=slug)
    
    # Check if user already liked this post
    if post.is_liked_by(request.user):
        # Unlike - remove user from likes
        post.likes.remove(request.user)
        liked = False
    else:
        # Like - add user to likes
        post.likes.add(request.user)
        liked = True
    
    # Return JSON response for AJAX
    return JsonResponse({
        'liked': liked,
        'total_likes': post.total_likes()
    })

@login_required
def add_comment(request, slug):
    """
    Add comment to a post
    Only logged in users can comment
    """
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'Error adding comment. Please try again.')
    
    return redirect('blog:post_detail', slug=slug)

@login_required
def delete_comment(request, comment_id):
    """
    Delete a comment - only comment author can delete
    """
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Security: Only comment author can delete
    if comment.author == request.user:
        post_slug = comment.post.slug
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect('blog:post_detail', slug=post_slug)
    else:
        messages.error(request, 'You can only delete your own comments.')
        return redirect('blog:home')
