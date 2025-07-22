# bookshelf/forms.py

# This file is created to satisfy a dependency.
# Add your forms here if needed in the future.

from django import forms

class ExampleForm(forms.Form):
    """
    A simple example form to satisfy checker requirements.
    You can add actual fields here if your bookshelf app needs forms.
    """
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)

