from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

class Posts(models.Model):
    title=models.CharField(max_length=25,blank=True)
    content=models.TextField(blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_user_id',null=True,default=0)
    def __str__(self):
        return self.title

class Comments(models.Model):
    name=models.CharField(max_length=25,blank=True)
    email=models.EmailField(max_length=30,blank=True)
    comment=models.TextField(blank=True)
    post_id=models.ForeignKey(Posts,on_delete=models.CASCADE,default=0,related_name='post_id')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_id',null=True,)

    def __str__(self):
        return self.name

