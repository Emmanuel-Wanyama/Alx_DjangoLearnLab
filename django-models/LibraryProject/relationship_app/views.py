from django.shortcuts import render
from django.http import HttpResponse
from .models import Book # Import the Book model

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

# Create your views here.
