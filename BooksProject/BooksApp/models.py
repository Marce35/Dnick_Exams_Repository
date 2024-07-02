from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    image = models.ImageField()
    pub_date = models.DateTimeField('date published')
    authors = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.name} - {self.book.title}"


class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
