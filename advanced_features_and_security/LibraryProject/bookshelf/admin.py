from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Displays these fields in the list view of the admin interface
    list_display = ('title', 'author', 'publication_year', 'id')

    # Adds filters to the right sidebar in the admin list view
    list_filter = ('publication_year', 'author')

    # Adds a search bar to the top of the admin list view
    # Searches across the specified fields
    search_fields = ('title', 'author')

    # Makes the fields clickable to view the detail page
    list_display_links = ('title',)

    # Fields that can be edited directly from the list view
    list_editable = ('publication_year',)

    # Order the list view by title by default
    ordering = ('title',)
