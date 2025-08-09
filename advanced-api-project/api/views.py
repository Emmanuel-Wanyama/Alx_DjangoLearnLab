# Import the specific generic views and permission classes from Django REST Framework.
from rest_framework import generics, permissions

# Import the models and serializers you've already defined.
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# -- Book Views --

# BookList view handles listing all books (GET requests).
# It allows both authenticated and unauthenticated users to read the data.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# BookCreate view handles creating a new book (POST requests).
# It only allows authenticated users to create new books.
class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # The perform_create hook is kept here to demonstrate customization.
    def perform_create(self, serializer):
        serializer.save()


# BookDetail view handles retrieving a single book (GET requests).
# It allows both authenticated and unauthenticated users to read the data.
class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# BookUpdate view handles updating a single book (PUT/PATCH requests).
# It only allows authenticated users to update books.
class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# BookDestroy view handles deleting a single book (DELETE requests).
# It only allows authenticated users to delete books.
class BookDestroy(generics.DestroyAPIView):
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


# AuthorDestroy view handles deleting a single author (DELETE requests).
class AuthorDestroy(generics.DeleteView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
