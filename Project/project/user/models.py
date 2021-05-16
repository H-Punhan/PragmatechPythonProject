from django.db import models
from django.db.models.fields import CharField, IntegerField,TextField


class Todos(models.Model):
    title=models.CharField(max_length=25)
    content=models.TextField()

# Create your models here.
