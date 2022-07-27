from dataclasses import dataclass
from django.shortcuts import render, redirect
from django.urls import reverse
from ELIB import models

from ELIB.forms import BookFormManager

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


def borrowed(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            records = models.BorrowedBook.objects.all().order_by('-borrowed')
        else:
            records = models.BorrowedBook.objects.filter(user=request.user).order_by('-borrowed')
        context_data = {
            'records': records
        }
        return render(request, 'elib/borrowed.html', context=context_data)

    return redirect(reverse('auth_app:home'))


def upload(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == "POST":
                form = BookFormManager(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect(reverse('ELIB:home-page'))
                return render(request, 'ELIB/upload.html', context={'form': form, 'error_msg': "Please valid data."})
            return render(request, 'ELIB/upload.html', context={'form': BookFormManager()})

        return redirect(reverse('ELIB:home-page'))

    return redirect(reverse('auth_app:home'))


def login(request):
    return render(request, 'login.html')


def librarian(request):
    return render(request, 'Librarian signup.html')


def student(request):
    return render(request, 'student signup.html')


