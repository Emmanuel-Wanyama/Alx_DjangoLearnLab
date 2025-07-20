# relationship_app/views.py

from django.shortcuts import render, redirect # Import redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm # Import UserCreationForm
from django.contrib.auth import login # Import login to automatically log in the user after registration


def list_books(request):
    """
    A function-based view that retrieves all books from the database
    and renders them using the 'relationship_app/list_books.html' template.
    """
    books = Book.objects.all().select_related('author')
    
    # Corrected template path: removed the redundant 'templates/'
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library,
    listing all books available in that library, using an HTML template.
    It uses Django's DetailView to retrieve a single Library object.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html' # This template is still needed for LibraryDetailView

    def get_context_data(self, **kwargs):
        """
        Add extra context to the template, specifically the books
        associated with the current library.
        """
        context = super().get_context_data(**kwargs)
        return context

def register(request):
    """
    Handles user registration.
    If the request method is POST, it attempts to create a new user.
    If successful, it logs the user in and redirects to the login redirect URL.
    Otherwise, it displays the registration form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately after registration
            return redirect('login_success') # Redirect to a success URL after login
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

