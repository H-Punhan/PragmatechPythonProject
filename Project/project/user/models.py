from django.db import models
from django.db.models.fields import CharField, IntegerField,TextField


class Todos(models.Model):
    title=models.CharField(max_length=25)
    viewers=models.IntegerField(default=0)
    content=models.TextField()

# Create your models here.
