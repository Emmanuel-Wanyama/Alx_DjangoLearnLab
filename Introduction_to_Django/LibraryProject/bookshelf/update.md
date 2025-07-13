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