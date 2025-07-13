## Delete Operation

    **Command:** Delete the book you created and confirm the deletion by trying to retrieve all books again.

    ```python
    book = Book.objects.get(title="Nineteen Eighty-Four")
    book.delete()
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
