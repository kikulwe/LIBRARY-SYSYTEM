from dataclasses import dataclass
from django.shortcuts import render, redirect
from django.urls import reverse
from elib import models

from elib.forms import BookFormManager

import datetime


# Create your views here.

def home(request):
    if request.GET.get('search', []):
        books = models.Book.objects.filter(title__contains=request.GET.get('search')).order_by('-id')
    else:
        books = models.Book.objects.all().order_by('-id')
    context_data = {
        'books': books
    }
    return render(request, 'elib/cover.html', context=context_data)


def details(request, slug):
    book = models.Book.objects.filter(slug=slug)[0]

    genres = models.Genre.objects.filter(book=book)

    context_data = {
        'book': book,
        'genres': genres
    }
    return render(request, 'elib/details.html', context=context_data)


def borrow(request, slug):
    if not request.user.is_authenticated:
        return redirect(reverse('auth_app:home'))

    # fetch book
    book = models.Book.objects.filter(slug=slug).first()
    if book.is_available:
        # do the borrowing
        # create an instance in the borrowed book table
        borrowed_book = models.BorrowedBook(user=request.user, book=book)

        # get return data after 30 days
        today = datetime.date.today()
        return_date = today + datetime.timedelta(days=30)
        borrowed_book.return_date = return_date

        # make book unavailable
        book.is_available = False
        book.save()

        # save borrowed book
        borrowed_book.save()

        return redirect(reverse('elib:borrowed'))




