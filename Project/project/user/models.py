from django.db import models
from django.db.models.fields import CharField, IntegerField



class User(models.Model):
    name=models.CharField(max_length=25)
    
class Images(models.Model):
    name=models.CharField(max_length=25)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)




# Create your models here.
