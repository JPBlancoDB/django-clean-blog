from django.db import models

from .author import Author


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    def __str__(self):
        return self.title
