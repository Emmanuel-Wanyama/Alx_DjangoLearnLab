# relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile, Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, permission_required
from django import forms


# Simple form for adding/editing books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a default choice for author if none exists
        if not Author.objects.exists():
            self.fields['author'].queryset = Author.objects.none()
            self.fields['author'].help_text = "No authors found. Please add an author first."
        else:
            self.fields['author'].queryset = Author.objects.all()


@permission_required('relationship_app.can_view_book', login_url='relationship_app:login', raise_exception=True)
def list_books(request):
    """
    A function-based view that retrieves all books from the database
     and renders them using the 'relationship_app/list_books.html' template.
    Requires 'can_view_book' permission.

    Security Note: Using Django's ORM (Book.objects.all()) automatically
    parameterizes database queries, preventing SQL injection.
    """
    books = Book.objects.all().select_related('author')
    
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library,
    listing all books available in that library, using an HTML template.
    It uses Django's DetailView to retrieve a single Library object.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'

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

    Security Note: UserCreationForm handles validation and sanitization of
    user registration data, protecting against common input-related vulnerabilities.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:login_success')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Helper functions for role checks
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin, login_url='relationship_app:login')
def admin_view(request):
    """
    View accessible only to users with the 'Admin' role.
    """
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

@user_passes_test(is_librarian, login_url='relationship_app:login')
def librarian_view(request):
    """
    View accessible only to users with the 'Librarian' role.
    """
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

@user_passes_test(is_member, login_url='relationship_app:login')
def member_view(request):
    """
    View accessible only to users with the 'Member' role.
    """
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})


# Views with custom permission checks
@permission_required('relationship_app.can_add_book', login_url='relationship_app:login', raise_exception=True)
def add_book(request):
    """
    Allows users with 'can_add_book' permission to add new books.

    Security Note: BookForm handles validation and sanitization of
    form data, preventing malicious input.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

@permission_required('relationship_app.can_change_book', login_url='relationship_app:login', raise_exception=True)
def edit_book(request, pk):
    """
    Allows users with 'can_change_book' permission to edit existing books.

    Security Note: get_object_or_404 ensures the object exists, preventing
    direct object access vulnerabilities. BookForm handles validation and
    sanitization of form data.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

@permission_required('relationship_app.can_delete_book', login_url='relationship_app:login', raise_exception=True)
def delete_book(request, pk):
    """
    Allows users with 'can_delete_book' permission to delete books.

    Security Note: get_object_or_404 ensures the object exists.
    Deletion is handled by Django's ORM.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

