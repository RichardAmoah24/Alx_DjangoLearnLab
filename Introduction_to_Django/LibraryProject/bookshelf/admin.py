from django.db import models
from .models import Book
"register", "admin.ModelAdmin"
class Book(models.Model):
   list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)

    def __str__(self):
        return self.title



