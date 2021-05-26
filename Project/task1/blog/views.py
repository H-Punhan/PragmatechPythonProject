from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *


def index(request):

    data={
        'data':Posts.objects.all()
    }
    
    return render(request,'index.html',data)

def create(request):
    
    if request.method=='POST':
        
        data=Posts(title=request.POST['title'],content=request.POST['content'])
        data.save()
        
        return redirect(index)
    return render(request,'add.html')

def read(request,id):
   
    data={
        'data':Posts.objects.get(id=id),
        'comments':Comments.objects.filter(post_id=id)
       
    }
    return render(request,'post.html',data)

def delete(request,id):
    
    data=Posts.objects.get(id=id).delete()
    return redirect(index)

def update(request,id):
    
    data=Posts.objects.get(id=id)
    content={
        'data':data
    }
    if request.method=='POST':
        data.title=request.POST['title']
        data.content=request.POST['content']
        data.save()
        return redirect(index)
    return render(request,'update.html',content)

def addcomment(request,id):
    
    if request.method=='POST':
        data=Comments(name=request.POST['name'],email=request.POST['email'],comment=request.POST['comment'],post_id=Posts.objects.get(id=id))
        data.save()
    
    return redirect(read,id=id)


# Create your views here.
