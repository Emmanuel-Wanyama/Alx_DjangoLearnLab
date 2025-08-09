# Import the path function from Django's URL configuration.
from django.urls import path

# Import the views you created in api/views.py.
from .views import BookListCreate, BookDetail

# Define the URL patterns for your API app.
urlpatterns = [
    # This path handles GET (list all books) and POST (create a new book) requests.
    # The name is optional but good practice for referencing the URL.
    path('books/', BookListCreate.as_view(), name='book-list-create'),

    # This path handles GET (retrieve a single book), PUT/PATCH (update),
    # and DELETE (delete) requests. The <int:pk> captures the book's primary key.
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
