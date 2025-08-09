from django.db import models

# The Author model stores information about a book's author.
# It has a single CharField for the author's name.
class Author(models.Model):
    # 'name' is the author's name, with a maximum length of 100 characters.
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The Book model stores information about a book.
# It has a title, publication year, and a link to its author.
class Book(models.Model):
    # 'title' is the book's title, with a maximum length of 200 characters.
    title = models.CharField(max_length=200)

    # 'publication_year' is an integer field for the year the book was published.
    publication_year = models.IntegerField()

    # The 'author' field is a ForeignKey to the Author model.
    # This creates a one-to-many relationship, meaning one author can have many books.
    # on_delete=models.CASCADE means that if an author is deleted, all their books are also deleted.
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
