from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# This view uses ListAPIView to handle GET requests and list all books.
class BookList(generics.ListAPIView):
    """
    API view to list all books.
    It uses the BookSerializer to serialize the queryset.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
