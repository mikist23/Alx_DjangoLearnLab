from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

class Book(models.model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    books = models.OneToOneField(Library, on_delete=models.CASCADE)