from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Detailed comments for the serializers as requested.

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer is responsible for converting Book model instances into JSON
    representations and vice-versa.
    
    It serializes all fields of the Book model and includes custom validation
    to prevent future publication years.
    
    This serializer is also used as a nested serializer inside the AuthorSerializer
    to show an author's books.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['author']  # Author is set by the nested serializer's logic.

    def validate_publication_year(self, value):
        """
        Custom validation to ensure that the publication_year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes the Author model.
    
    It handles the one-to-many relationship by including a nested BookSerializer.
    The `books` field, which corresponds to the `related_name` in the ForeignKey
    of the Book model, is dynamically serialized using the BookSerializer.
    This creates a nested representation where an author's details and their
    list of books are returned in a single response.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
