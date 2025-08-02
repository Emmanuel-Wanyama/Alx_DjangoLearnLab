from rest_framework import serializers
from .models import Book

# The BookSerializer class converts Book model instances to JSON and vice versa.
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """
    class Meta:
        # Link the serializer to the Book model.
        model = Book
        # Include all fields from the Book model in the serialization.
        fields = '__all__'
