from django.db import models
from .models import Book
"register", "admin.ModelAdmin"
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


