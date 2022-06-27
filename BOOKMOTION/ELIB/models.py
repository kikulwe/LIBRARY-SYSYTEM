from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(verbose_name="Author's Name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



