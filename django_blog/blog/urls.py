'''from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
'''

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # URL for viewing all posts
    path('posts/', PostListView.as_view(), name='post-list'),

    # URL for creating a new post
    path('posts/new/', PostCreateView.as_view(), name='post-create'),

    # URL for viewing a specific post's details
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # URL for editing an existing post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),

    # URL for deleting a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]