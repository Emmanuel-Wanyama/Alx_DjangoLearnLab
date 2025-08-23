from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    The author is a read-only field, automatically set to the logged-in user.
    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    Includes nested comments and sets the author as a read-only field.
    """
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']
