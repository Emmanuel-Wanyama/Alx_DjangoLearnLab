from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

# Define a test suite for your Book API views.
class BookAPITests(APITestCase):
    # The setUp method runs before each test method.
    # It's used to create a clean environment for each test.
    def setUp(self):
        # Create a test user for authenticated requests.
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a sample author and book for testing.
        self.author = Author.objects.create(name='Frank Herbert')
        self.book_data = {'title': 'Dune', 'publication_year': 1965, 'author': self.author.id}
        self.book = Book.objects.create(**self.book_data)

        # Define the URLs for the book list and detail views.
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    # --- CRUD Operation Tests ---

    # Test that an unauthenticated user can list books.
    def test_unauthenticated_user_can_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test that an unauthenticated user cannot create a book.
    def test_unauthenticated_user_cannot_create_book(self):
        response = self.client.post(self.create_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 1)

    # Test that an authenticated user can create a book.
    def test_authenticated_user_can_create_book(self):
        self.client.login(username='testuser', password='testpassword')
        new_book_data = {'title': 'Foundation', 'publication_year': 1951, 'author': self.author.id}
        response = self.client.post(self.create_url, new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data['title'], 'Foundation')
    
    # Test that an unauthenticated user can retrieve a book.
    def test_unauthenticated_user_can_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Dune')
    
    # Test that an unauthenticated user cannot update a book.
    def test_unauthenticated_user_cannot_update_book(self):
        updated_data = {'title': 'Dune Messiah'}
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Dune') # Ensure title didn't change
        
    # Test that an authenticated user can update a book.
    def test_authenticated_user_can_update_book(self):
        self.client.login(username='testuser', password='testpassword')
        updated_data = {'title': 'Dune Messiah', 'publication_year': 1969, 'author': self.author.id}
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Dune Messiah')
        
    # Test that an unauthenticated user cannot delete a book.
    def test_unauthenticated_user_cannot_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 1)
        
    # Test that an authenticated user can delete a book.
    def test_authenticated_user_can_delete_book(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
        
    # --- Advanced Query Tests ---

    # Test that the API can filter books by title.
    def test_book_list_filter_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Dune'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')
    
    # Test that the API can search books by title and author name.
    def test_book_list_search_by_title_and_author(self):
        # Search by book title.
        response_title = self.client.get(self.list_url, {'search': 'Dune'})
        self.assertEqual(response_title.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_title.data), 1)
        
        # Search by author name.
        response_author = self.client.get(self.list_url, {'search': 'Frank'})
        self.assertEqual(response_author.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_author.data), 1)

    # Test that the API can order books by a field.
    def test_book_list_ordering(self):
        Book.objects.create(title='Children of Dune', publication_year=1976, author=self.author)
        
        # Test ordering by title descending.
        response = self.client.get(self.list_url, {'ordering': '-title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Dune')
        self.assertEqual(response.data[1]['title'], 'Children of Dune')
        
        # Test ordering by publication year ascending.
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Dune')
        self.assertEqual(response.data[1]['title'], 'Children of Dune')
