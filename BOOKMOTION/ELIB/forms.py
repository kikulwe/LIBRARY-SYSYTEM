from django.forms import ModelForm
from django import forms

from .models import Book, Genre


class BookFormManager(ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'genre'}),
    )

class Meta:
    fields = ('title', 'description', 'author', 'cover')
    model = Book

def __init__(self, *args, **kwargs):
    super(BookFormManager, self).__init__(*args, **kwargs)

    for visible in self.visible_fields():
        visible.field.widget.attrs['class'] = 'form-control form-control-lg'

