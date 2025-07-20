# relationship_app/query_samples.py

import os
import django

# Configure Django settings
# You need to replace 'your_project_name.settings' with the actual path to your settings file.
# In your case, it's likely 'django_models.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    """
    Demonstrates various queries on the defined Django models
    to showcase ForeignKey, ManyToMany, and OneToOne relationships.
    """
    print("--- Running Relationship Query Samples ---")

    # --- 1. Query all books by a specific author ---
    print("\n1. Querying all books by a specific author:")
    try:
        # Create some sample data if it doesn't exist
        author1, created = Author.objects.get_or_create(name="Jane Austen")
        if created:
            print(f"Created Author: {author1.name}")
        book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
        if created:
            print(f"Created Book: {book1.title}")
        book2, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)
        if created:
            print(f"Created Book: {book2.title}")

        # Query books by author's name
        target_author_name = "Jane Austen"
        try:
            author = Author.objects.get(name=target_author_name)
            books_by_author = author.books.all() # Using the related_name 'books'
            print(f"Books by {target_author_name}:")
            if books_by_author.exists():
                for book in books_by_author:
                    print(f"  - {book.title}")
            else:
                print(f"  No books found for {target_author_name}.")
        except Author.DoesNotExist:
            print(f"Author '{target_author_name}' not found.")

    except Exception as e:
        print(f"Error during author/book query: {e}")


    # --- 2. List all books in a library ---
    print("\n2. Listing all books in a library:")
    try:
        # Create some sample data if it doesn't exist
        library1, created = Library.objects.get_or_create(name="Central City Library")
        if created:
            print(f"Created Library: {library1.name}")

        # Ensure books are added to the library
        library1.books.add(book1, book2) # Add the books created earlier
        print(f"Added books to {library1.name}")

        # Query books in a library by library's name
        library_name = "Central City Library" # Changed variable name
        try:
            library = Library.objects.get(name=library_name) # Used new variable name
            books_in_library = library.books.all() # Using the ManyToManyField 'books'
            print(f"Books in {library_name}:")
            if books_in_library.exists():
                for book in books_in_library:
                    print(f"  - {book.title} by {book.author.name}")
            else:
                print(f"  No books found in {library_name}.")
        except Library.DoesNotExist:
            print(f"Library '{library_name}' not found.")

    except Exception as e:
        print(f"Error during library/books query: {e}")


    # --- 3. Retrieve the librarian for a library ---
    print("\n3. Retrieving the librarian for a library:")
    try:
        # Create some sample data if it doesn't exist
        # Ensure library1 exists from previous step
        librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", library=library1)
        if created:
            print(f"Created Librarian: {librarian1.name} for {library1.name}")

        # Query librarian by library's name
        library_name = "Central City Library" # Changed variable name
        try:
            library = Library.objects.get(name=library_name) # Used new variable name
            # Access the librarian through the related_name 'librarian'
            librarian = library.librarian
            print(f"Librarian for {library_name}: {librarian.name}")
        except Library.DoesNotExist:
            print(f"Library '{library_name}' not found.")
        except Librarian.DoesNotExist:
            print(f"No librarian found for '{library_name}'.")

    except Exception as e:
        print(f"Error during librarian query: {e}")

    print("\n--- Query Samples Finished ---")

if __name__ == "__main__":
    run_queries()
