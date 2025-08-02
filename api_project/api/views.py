from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Book
from .serializers import BookSerializer

# This view is for listing all books or creating a new one.
# It uses the IsAuthenticatedOrReadOnly permission, meaning:
# - Authenticated users can perform any action (GET, POST, PUT, DELETE).
# - Unauthenticated users can only perform read-only actions (GET).
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# This viewset automatically provides `list`, `create`, `retrieve`,
# `update`, and `destroy` actions.
# It also uses the IsAuthenticatedOrReadOnly permission.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# This is an example of a view restricted to admin users only.
# Only users with the `is_staff` attribute set to True can access this.
class AdminBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]



# Create your views here.
