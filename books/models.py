from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField()
    author = models.CharField(max_length=50)


class Thread(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=100)
    content = models.TextField()
    reading_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
