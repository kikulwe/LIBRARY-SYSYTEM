from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(verbose_name="Author's Name", max_length=100)
    added_on = models.DateField(verbose_name="Added On",default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    title = models.CharField("Title",max_length=150)
    author = models.ForeignKey(to=Author,on_delete=models.CASCADE,)
    genres = models.ManyToManyField(Genre)
    is_available = models.BooleanField(verbose_name="Is Available",default=True)
    added_on = models.DateField(verbose_name="Added On",default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class BorrowedBook(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    book = models.OneToOneField(Book,on_delete=models.CASCADE,related_name='book')
    return_date = models.DateField('Return Date')
    borrowed = models.DateField(verbose_name="Borrowed On",default=timezone.now)
    fine = models.IntegerField('Fine',default=0)





