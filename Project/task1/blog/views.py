from django.forms.forms import Form
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    userid=User.objects.get(username=request.user)
    getdata=Posts.objects.filter(user_id=userid.id)
    
    data={
        'data':getdata
    }
    
    return render(request,'index.html',data)
@login_required
def create(request):
    
    if request.method=='POST':
        userid=User.objects.get(username=request.user)
        data=Posts(title=request.POST['title'],content=request.POST['content'],user_id=userid.id)
        data.save()
        
        
    print(request.user)
    return render(request,'add.html')
@login_required
def read(request,id):
   
    data={
        'data':Posts.objects.get(id=id),
        'comments':Comments.objects.filter(post_id=id)
       
    }
    return render(request,'post.html',data)
@login_required
def delete(request,id):
    
    data=Posts.objects.get(id=id).delete()
    return redirect(index)
@login_required
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
@login_required
def addcomment(request,id):
    
    if request.method=='POST':
        data=Comments(name=request.POST['name'],email=request.POST['email'],comment=request.POST['comment'],post_id=Posts.objects.get(id=id))
        data.save()
    
    return redirect(read,id=id)

def userlogin(request):
    if request.method=='POST':
        data=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if data is not None:
            login(request, data)
            return HttpResponse('admin')
        else:
            return HttpResponse('---')
    
    return render(request,'login.html')
@login_required
def test(request):
    return HttpResponse('admin')

@login_required()
def logoutuser(request):
    logout(request)
    return redirect(userlogin)
# Create your views here.
