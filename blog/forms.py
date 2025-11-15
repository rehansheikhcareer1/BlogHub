from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    """
    Form for creating and editing blog posts
    Includes all necessary fields with proper styling
    """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'tags', 'content', 'excerpt', 'featured_image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter an engaging title for your post'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'url-friendly-slug (auto-fills from title)'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': '5'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 15,
                'placeholder': 'Write your amazing content here...',
                'style': 'font-family: monospace; font-size: 14px;'
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief summary (shown in post previews)'
            }),
            'featured_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class CommentForm(forms.ModelForm):
    """
    Form for adding comments to blog posts
    Simple and user-friendly
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your thoughts...',
                'style': 'resize: none;'
            }),
        }
        labels = {
            'content': ''
        }
