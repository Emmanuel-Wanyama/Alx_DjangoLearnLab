'''from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Post, Comment

class UserRegisterForm(UserCreationForm):
    """
    A form for user registration with an email field.
    """
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    """
    A form for authenticated users to update their username and email.
    """
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    A form for authenticated users to update their profile picture.
    """
    class Meta:
        model = Profile
        fields = ['image']

class PostForm(forms.ModelForm):
    """
    A form for creating and updating blog posts based on the Post model.
    """
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class CommentForm(forms.ModelForm):
    """
    A form for creating and updating comments based on the Comment model.
    """
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Your Comment',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from taggit.forms import TagField # Import TagField

class UserRegisterForm(UserCreationForm):
    """
    A form for user registration with an email field.
    """
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    """
    A form for authenticated users to update their username and email.
    """
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """
    A form for authenticated users to update their profile picture.
    """
    class Meta:
        model = Profile
        fields = ['image']

class PostForm(forms.ModelForm):
    """
    A form for creating and updating blog posts based on the Post model.
    """
    tags = TagField(label="Tags (comma-separated)", required=False) # Add tags field

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags'] # Include tags in the fields
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class CommentForm(forms.ModelForm):
    """
    A form for creating and updating comments based on the Comment model.
    """
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Your Comment',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

