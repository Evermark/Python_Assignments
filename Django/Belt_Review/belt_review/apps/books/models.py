from __future__ import unicode_literals
from django.db import models
from ..login.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name ="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    text = models.TextField()
    stars = models.SmallIntegerField(0)
    book = models.ForeignKey(Book, related_name ="reviews")
    user = models.ForeignKey(User, related_name ="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
