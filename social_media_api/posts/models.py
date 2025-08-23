from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    """
    Represents a blog post created by a user.
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the post, which is its title.
        """
        return self.title

class Comment(models.Model):
    """
    Represents a comment made by a user on a specific post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the comment, indicating the author and post.
        """
        return f'Comment by {self.author.username} on {self.post.title}'

class Like(models.Model):
    """
    Model to track post likes.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user') # Ensures a user can only like a post once.

    def __str__(self):
        return f'Like by {self.user} on {self.post}'