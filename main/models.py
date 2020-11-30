from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"{self.title}-{self.description}"

class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(max_length=25)
    def __repr__(self):
        return f"{self.first_name}-{self.last_name}"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.


