from django.db import models

class Posts(models.Model):
    title=models.CharField(max_length=25,blank=True)
    content=models.TextField(blank=True)

