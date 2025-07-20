# Django Shell CRUD Operations for Book Model

    ## Setup: Import the Book Model
    ```python
    from bookshelf.models import Book
    ```
    *Output:* (No explicit output, just loads the model)

    ---

    ## Create Operation

    **Command:** Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.

    ```python
    book_1984 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
    print(book_1984)
    ```

    **Output:**
    ```
    1984 by George Orwell (1949)
    ```
    *(Note: The exact ID might vary, but the string representation will be similar.)*

    ---

    ## Retrieve Operation

    **Command:** Retrieve and display all attributes of the book you just created.

    ```python
    retrieved_book = Book.objects.get(title="1984")
    print(f"Title: {retrieved_book.title}")
    print(f"Author: {retrieved_book.author}")
    print(f"Publication Year: {retrieved_book.publication_year}")
    print(f"ID: {retrieved_book.id}")
    ```

    **Output:**
    ```
    Title: 1984
    Author: George Orwell
    Publication Year: 1949
    ID: 1
    ```
    *(Note: The ID will match the one assigned during creation.)*

    ---

    ## Update Operation

    **Command:** Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

    ```python
    book_to_update = Book.objects.get(title="1984")
    book_to_update.title = "Nineteen Eighty-Four"
    book_to_update.save()
    print(book_to_update)
    ```

    **Output:**
    ```
    Nineteen Eighty-Four by George Orwell (1949)
    ```

    ---

    ## Delete Operation

    **Command:** Delete the book you created and confirm the deletion by trying to retrieve all books again.

    ```python
    book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
    book_to_delete.delete()
    print("Book deleted.")

    all_books_after_delete = Book.objects.all()
    print("All books after deletion:")
    for book in all_books_after_delete:
        print(book)
    if not all_books_after_delete:
        print("No books found.")
    ```

    **Output:**
    ```
    Book deleted.
    All books after deletion:
    No books found.
    ```
