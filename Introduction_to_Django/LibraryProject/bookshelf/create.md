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
