from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.utils.text import slugify
import os
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (instance.slug, uuid.uuid4(), ext)
    return os.path.join('books/', filename)


class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(verbose_name="Author's Name", max_length=100)
    added_on = models.DateField(verbose_name="Added On", default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-added_on']


class Book(models.Model):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description")
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    is_available = models.BooleanField(verbose_name="Is Available", default=True)
    cover = models.ImageField(
        verbose_name=_('Cover'),
        upload_to=get_file_path,
        default='./books/ELIB_book.wep3'
    )
    slug = models.SlugField(
        _("Safe Url"),
        unique=True,
        blank=True,
        null=True,
    )
    added_on = models.DateField(verbose_name="Added On", default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:50])

        self.title = self.title.title()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_on']


class BorrowedBook(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='book')
    return_date = models.DateField('Return Date', blank=True, null=True)
    borrowed = models.DateField(verbose_name="Borrowed On", default=timezone.now)
    fine = models.IntegerField('Fine', default=0)

    def __str__(self):
        return "{} - {}".format(self.book.title, self.user.username)


@receiver(post_delete, sender=BorrowedBook)
def signal_function_name(sender, instance, using, **kwargs):
    book = instance.book
    book.is_available = True
    book.save()


