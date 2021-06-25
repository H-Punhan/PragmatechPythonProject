from django.db import models
from django.contrib.auth.models import User



# Blog ucun olan model
class Blogs(models.Model):
    title=models.CharField(max_length=50,blank=True)
    content=models.TextField(blank=True)
    image=models.FileField(upload_to='static/assets/img')
    postdate=models.DateField(auto_now=True)
    author=models.ForeignKey(User,blank=True,on_delete=models.CASCADE)

# Tag modeli
class Tags(models.Model):
    name=models.CharField(max_length=25,blank=True)

# Blog ucun olan taglar 
class Blogtags(models.Model):
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='blog_id',blank=True)
    tag=models.ForeignKey(Tags,on_delete=models.CASCADE,related_name='tag_id',blank=True)
    
# Commentler
class Blogcomments(models.Model):
    name=models.CharField(max_length=25,blank=True)
    message=models.TextField(blank=True)
    email=models.EmailField(blank=True)
    blog=models.ForeignKey(Blogs,blank=True,on_delete=models.CASCADE,related_name='comment_blog_id')

