# Import the generic views and permission classes from Django REST Framework.
from rest_framework import generics, permissions

# Import the models and serializers you've already defined.
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# This view handles listing all books and creating a new book.
# We've added a permission_classes attribute to enforce authentication.
class BookListCreate(generics.ListCreateAPIView):
    # This permission class allows any user to read (GET requests),
    # but only authenticated users to create (POST requests).
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # This method is an example of customizing the create behavior.
    # It allows you to run additional logic before a new object is saved.
    # For instance, you could set the book's author to the current user.
    def perform_create(self, serializer):
        # In a real-world scenario, you would need to associate the author
        # with the logged-in user. For this example, we'll assume the
        # user exists and is a valid author. You'd need to handle this logic
        # and validation in your actual application.
        # Example: serializer.save(author=self.request.user.author)
        serializer.save()


# This view handles retrieving, updating, and deleting a single Book instance.
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    # We use the same permission class here to allow only authenticated users
    # to update or delete a book.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# This view lists all authors and allows for the creation of a new author.
class AuthorListCreate(generics.ListCreateAPIView):
    # We apply the same permission class to the Author views.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# This view handles retrieving, updating, and deleting a single Author instance.
# It also uses the AuthorSerializer, which includes the nested books.
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    # We apply the same permission class to the Author views.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
