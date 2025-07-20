from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def list_books(request):
        """
        A function-based view that retrieves all books from the database
        and renders them as a simple plain text list of titles and authors.
        """
        books = Book.objects.all().select_related('author')
        
        # Build a simple plain text string with book titles and authors
        book_titles_authors = "All Books in the Database:\n\n"
        if books:
            for book in books:
                book_titles_authors += f"- {book.title} by {book.author.name}\n"
        else:
            book_titles_authors += "No books found in the database.\n"
            
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