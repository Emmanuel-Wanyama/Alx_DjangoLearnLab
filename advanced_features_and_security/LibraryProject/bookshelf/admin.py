# relationship_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin # Import default UserAdmin
from .models import CustomUser, UserProfile, Author, Book, Library, Librarian # Import your models

# Custom Admin for CustomUser
class CustomUserAdmin(DefaultUserAdmin):
    """
    Admin configuration for the CustomUser model.
    Adds date_of_birth and profile_photo to the user change form.
    """
    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = DefaultUserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # You might want to add 'date_of_birth' and 'profile_photo' to list_display
    list_display = DefaultUserAdmin.list_display + ('date_of_birth', 'profile_photo')


# Unregister the default User model if it was registered
try:
    admin.site.unregister(admin.site.get_model('auth', 'User'))
except admin.sites.NotRegistered:
    pass # Already unregistered or not registered

# Register your CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

# Register other models as usual
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(CustomUser, CustomUserAdmin)

