from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# Custom User Manager
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)


# Custom User Model
class CustomUser(AbstractUser):
    """
    Custom User model extending AbstractUser with additional fields.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email', 'date_of_birth']

    def __str__(self):
        return self.username


# Author Model:
# name: CharField.
class Author(models.Model):
    """
    Represents an author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model:
# title: CharField.
# author: ForeignKey to Author.
class Book(models.Model):
    """
    Represents a book.
    Each book is written by one author (ForeignKey).
    """
    title = models.CharField(max_length=200)
    # ForeignKey: A Book belongs to one Author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        # Define custom permissions for the Book model
        permissions = [
            ("can_view_book", "Can view book"), # New permission
            ("can_create", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

# Library Model:
# name: CharField.
# books: ManyToManyField to Book.
class Library(models.Model):
    """
    Represents a library.
    A library can have many books, and a book can be in many libraries.
    """
    name = models.CharField(max_length=100, unique=True)
    # ManyToManyField: A Library can have many Books, and a Book can be in many Libraries
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# Librarian Model:
# name: CharField.
# library: OneToOneField to Library.
class Librarian(models.Model):
    """
    Represents a librarian.
    Each librarian is associated with one library (OneToOneField).
    """
    name = models.CharField(max_length=100)
    # OneToOneField: Links directly to a Library
    # on_delete=models.CASCADE means if the Library is deleted, the Librarian is also deleted.
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"Librarian: {self.name} ({self.library.name})"

# UserProfile Model: Extends Django's User model with a role
class UserProfile(models.Model):
    """
    Extends Django's built-in User model to include a role.
    Now linked to the CustomUser model.
    """
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    # Link to the custom user model using settings.AUTH_USER_MODEL
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"

# Signal to automatically create a UserProfile when a new CustomUser is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    # Ensure a userprofile exists before trying to save it
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()