from django.db import models

class Book(models.Model):
    """
    A simple model representing a book.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the book, which is its title.
        This is helpful for the Django admin interface.
        """
        return self.title

# Create your models here.
