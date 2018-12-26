from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateField()

    def __str__(self):
        return self.name

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.filter(pk=id).values().first()

    @classmethod
    def get_list(cls):
        return list(cls.objects.values())
