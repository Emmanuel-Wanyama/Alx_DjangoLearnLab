from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Authors.
    
    This provides endpoints for listing all authors, creating a new author,
    retrieving a single author, updating an author, and deleting an author.
    The serializer handles the nested books display automatically.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Books.
    
    This provides endpoints for all CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
