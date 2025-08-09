from django.urls import path

from .views import (
    AuthorList, AuthorCreate, AuthorDetail, AuthorUpdate, AuthorDestroy,
    BookList, BookCreate, BookDetail, BookUpdate, BookDestroy
)

urlpatterns = [
    # Book URLs
    path('books/', BookList.as_view(), name='book-list'),
    path('books/create/', BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDestroy.as_view(), name='book-delete'),

    # Author URLs
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/create/', AuthorCreate.as_view(), name='author-create'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('authors/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', AuthorDestroy.as_view(), name='author-delete'),
]
