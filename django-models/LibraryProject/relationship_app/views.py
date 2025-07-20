from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView # Import DetailView
from .models import Book, Library # Import Library model

def book_list(request):
    """
    A function-based view that retrieves all books from the database
    and renders them as a simple text list of titles and authors.
    """
    books = Book.objects.all().select_related('author') # Select related author to avoid N+1 queries
    
    # Build a string with book titles and authors
    book_titles_authors = "<h1>All Books in the Database</h1>"
    if books:
        book_titles_authors += "<ul>"
        for book in books:
            book_titles_authors += f"<li>{book.title} by {book.author.name}</li>"
        book_titles_authors += "</ul>"
    else:
        book_titles_authors += "<p>No books found in the database.</p>"
        
    return HttpResponse(book_titles_authors)

class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library,
    listing all books available in that library.
    It uses Django's DetailView to retrieve a single Library object.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html' # This view should render a simple text list of book titles and their authors.

    def get_context_data(self, **kwargs):
        """
        Add extra context to the template, specifically the books
        associated with the current library.
        """
        context = super().get_context_data(**kwargs)
        # The 'object' in context is the Library instance retrieved by DetailView
        context['books_in_library'] = self.object.books.all().select_related('author')
        return context

# Create your views here.
