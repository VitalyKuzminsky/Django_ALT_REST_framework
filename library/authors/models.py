from django.db import models
from uuid import uuid4
# Create your models here.


class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        name = f'{self.first_name} {self.last_name}'
        return name


class Biographies(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)
