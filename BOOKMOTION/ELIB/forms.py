from django.forms import ModelForm
from django import forms

from .models import Book, Genre


class BookFormManager(ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'genre'}),
    )
