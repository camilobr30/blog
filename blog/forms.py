from dataclasses import fields
from pyexpat import model
from django import forms

from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'content')