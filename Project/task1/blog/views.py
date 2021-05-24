from django.shortcuts import redirect, render
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
        'data':Posts.objects.get(id=id)
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


# Create your views here.
