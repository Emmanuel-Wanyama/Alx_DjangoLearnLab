from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile # Import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test # Import user_passes_test


def list_books(request):
    """
    A function-based view that retrieves all books from the database
    and renders them using the 'relationship_app/list_books.html' template.
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
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # UserProfile is created automatically by signal, no need to manually create here
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

