# Import necessary modules from Django REST Framework.
from rest_framework import serializers
from datetime import date

# Import the models we created in api/models.py.
from .models import Author, Book

# This is the serializer for the Book model.
# It handles converting Book model instances to JSON and vice versa.
class BookSerializer(serializers.ModelSerializer):
    # Custom validation for the publication_year field.
    def validate_publication_year(self, value):
        # We check if the provided year is in the future.
        if value > date.today().year:
            # If the year is in the future, we raise a validation error.
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    # The Meta class specifies which model to use and which fields to include.
    class Meta:
        model = Book
        # We specify all fields to be serialized.
        fields = '__all__'

# This is the serializer for the Author model.
# It includes a nested serializer for the related books.
class AuthorSerializer(serializers.ModelSerializer):
    # This line creates a nested BookSerializer.
    # 'many=True' indicates that an author can have multiple books.
    # 'read_only=True' means this field will not be used for creating or updating an author;
    # it is only for display purposes. The 'books' attribute comes from the
    # related_name='books' we defined in the Book model's ForeignKey.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # We specify the fields to be serialized, including the nested 'books' field.
        fields = ['id', 'name', 'books']
