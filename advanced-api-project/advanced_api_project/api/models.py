from django.db import models

# Detailed comments for the models as requested.

class Author(models.Model):
    """
    The Author model represents a person who has written one or more books.
    
    This model serves as the 'one' side of the one-to-many relationship with the Book model.
    It contains a single field, 'name', to store the author's full name.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a single book.
    
    It contains fields for the book's title, publication year, and a foreign key
    to the Author model, linking each book to a specific author. The related_name
    'books' allows us to easily access all books associated with an author
    from the Author instance itself.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # Establishes a one-to-many relationship. A single Author can have many Books.
    # The `on_delete=models.CASCADE` ensures that if an Author is deleted,
    # all of their associated books are also deleted.
    # `related_name='books'` allows us to access an author's books via `author_instance.books.all()`.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"
