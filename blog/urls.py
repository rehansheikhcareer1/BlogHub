from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    
    # Post CRUD operations
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit/', views.post_update, name='post_update'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    
    # Category filtering
    path('category/<slug:slug>/', views.category_posts, name='category'),
    
    # User dashboard
    path('my-posts/', views.my_posts, name='my_posts'),
    
    # Engagement features
    path('post/<slug:slug>/like/', views.post_like, name='post_like'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
