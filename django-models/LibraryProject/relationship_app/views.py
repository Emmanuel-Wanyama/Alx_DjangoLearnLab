# relationship_app/views.py

from django.shortcuts import render # Keep render for other potential uses, though not for book_list now
from django.http import HttpResponse # Ensure HttpResponse is imported
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library # Import Library model

def book_list(request):
    """
    A function-based view that retrieves all books from the database
    and renders them as a simple plain text list of titles and authors.
    """
    books = Book.objects.all().select_related('author') # Select related author to avoid N+1 queries
    
    # Build a simple plain text string with book titles and authors
    book_titles_authors = "All Books in the Database:\n\n"
    if books:
        for book in books:
            book_titles_authors += f"- {book.title} by {book.author.name}\n"
    else:
        book_titles_authors += "No books found in the database.\n"
        
    return HttpResponse(book_titles_authors, content_type="text/plain")

class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library,
    listing all books available in that library, using an HTML template.
    It uses Django's DetailView to retrieve a single Library object.
    """
    model = Library
    template_name = 'relationship_app/list_books.html' # Path to your template
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """
        Add extra context to the template, specifically the books
        associated with the current library.
        """
        context = super().get_context_data(**kwargs)
        # The 'object' in context is the Library instance retrieved by DetailView
        # The template can access books directly via {{ library.books.all }}
        # but explicitly adding it to context can sometimes be clearer.
        # For ManyToMany, accessing directly in template is usually fine.
        # context['books_in_library'] = self.object.books.all().select_related('author')
        return context

