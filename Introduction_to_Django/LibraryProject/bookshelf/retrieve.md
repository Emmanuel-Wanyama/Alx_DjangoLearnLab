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
