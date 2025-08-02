from django.urls import path
from .views import BookList

# URL patterns for the API app.
urlpatterns = [
    # This path maps 'books/' to the BookList view.
    path('books/', BookList.as_view(), name='book-list'),
]
