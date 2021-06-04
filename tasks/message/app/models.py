from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='sender_id')
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='owner_id')
    message=models.TextField()

# Create your models here.
