from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Books
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Books)