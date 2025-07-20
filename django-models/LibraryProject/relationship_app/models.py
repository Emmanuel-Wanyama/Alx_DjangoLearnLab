from django.db import models

# Author Model:
# name: CharField.
class Author(models.Model):
    """
    Represents an author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model:
# title: CharField.
# author: ForeignKey to Author.
class Book(models.Model):
    """
    Represents a book.
    Each book is written by one author (ForeignKey).
    """
    title = models.CharField(max_length=200)
    # ForeignKey: A Book belongs to one Author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# Library Model:
# name: CharField.
# books: ManyToManyField to Book.
class Library(models.Model):
    """
    Represents a library.
    A library can have many books, and a book can be in many libraries.
    """
    name = models.CharField(max_length=100, unique=True)
    # ManyToManyField: A Library can have many Books, and a Book can be in many Libraries
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# Librarian Model:
# name: CharField.
# library: OneToOneField to Library.
class Librarian(models.Model):
    """
    Represents a librarian.
    Each librarian is associated with one library (OneToOneField).
    """
    name = models.CharField(max_length=100)
    # OneToOneField: Links directly to a Library
    # on_delete=models.CASCADE means if the Library is deleted, the Librarian is also deleted.
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"Librarian: {self.name} ({self.library.name})"



# Create your models here.
