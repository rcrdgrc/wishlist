from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.description