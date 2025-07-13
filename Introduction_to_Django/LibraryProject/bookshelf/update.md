## Update Operation

    **Command:** Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

    ```python
    book = Book.objects.get(title="1984")
    book.title = "Nineteen Eighty-Four"
    book.save()
    print(book)
    ```

    **Output:**
    ```
    Nineteen Eighty-Four by George Orwell (1949)
    ```