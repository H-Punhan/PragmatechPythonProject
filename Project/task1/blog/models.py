from django.db import models
from django.db.models.base import Model

class Posts(models.Model):
    title=models.CharField(max_length=25,blank=True)
    content=models.TextField(blank=True)
    def __str__(self):
        return self.title

class Comments(models.Model):
    name=models.CharField(max_length=25,blank=True)
    email=models.EmailField(max_length=30,blank=True)
    comment=models.TextField(blank=True)
    post_id=models.ForeignKey(Posts,on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.name

