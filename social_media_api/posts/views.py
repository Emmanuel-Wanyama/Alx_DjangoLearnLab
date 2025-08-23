from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from django.db import IntegrityError

from .models import Post, Comment, Like # Import the new Like model
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification # Import the Notification model
from django.contrib.contenttypes.models import ContentType

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        """
        Sets the author of the post to the current logged-in user.
        """
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        """
        Sets the author of the comment to the current logged-in user.
        """
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    """
    API view to display a feed of posts from users the current user follows.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        # Get the IDs of users the current user is following
        followed_users = user.following.all()
        # Filter posts to include only those from followed users
        # and order them by creation date, newest first
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
    
    '''Post.objects.filter(author__in=following_users).order_by", "permissions.IsAuthenticated'''

class LikeView(APIView):
    """
    API view to like a post.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        try:
            Like.objects.create(post=post, user=user)
            if post.author != user:
                # Create a notification for the post author
                Notification.objects.create(
                    recipient=post.author,
                    actor=user,
                    verb='liked',
                    target=post
                )
            return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_409_CONFLICT)

class UnlikeView(APIView):
    """
    API view to unlike a post.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        like = Like.objects.filter(post=post, user=user).first()
        if like:
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
        
        return Response({"message": "You have not liked this post."}, status=status.HTTP_404_NOT_FOUND)

'''"generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)"'''