# Import the specific generic views and permission classes from Django REST Framework.
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter # Import the filtering backend
from django_filters import rest_framework

# Import the models and serializers you've already defined.
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# -- Book Views --

class BookList(generics.ListView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # We've added SearchFilter to the filter_backends list.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # We specify the fields that can be used for filtering.
    # The API will now accept queries like ?title=Dune or ?author=1.
    filterset_fields = ['title', 'author', 'publication_year']
    
    # This attribute specifies which fields to search on.
    # We are enabling search on the book's title and the author's name.
    # The double-underscore syntax ('author__name') is used to traverse the foreign key relationship.
    search_fields = ['title', 'author__name']


    # We specify the fields that can be used for ordering the results.
    # The API will now accept queries like ?ordering=title or ?ordering=-publication_year.
    ordering_fields = ['title', 'publication_year']


# BookCreate view handles creating a new book (POST requests).
class BookCreate(generics.CreateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# BookDetail view handles retrieving a single book (GET requests).
class BookDetail(generics.DetailView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# BookUpdate view handles updating a single book (PUT/PATCH requests).
class BookUpdate(generics.UpdateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# BookDestroy view handles deleting a single book (DELETE requests).
class BookDestroy(generics.DeleteView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# -- Author Views --

# AuthorList view handles listing all authors (GET requests).
class AuthorList(generics.ListView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# AuthorCreate view handles creating a new author (POST requests).
class AuthorCreate(generics.CreateView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


# AuthorDetail view handles retrieving a single author (GET requests).
class AuthorDetail(generics.DetailView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# AuthorUpdate view handles updating a single author (PUT/PATCH requests).
class AuthorUpdate(generics.UpdateView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


# AuthorDestroy view handles deleting a single book (DELETE requests).
class AuthorDestroy(generics.DeleteView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
