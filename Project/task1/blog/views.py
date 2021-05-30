from django.forms.forms import Form
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *

from django.db.models import Q
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    userid=User.objects.get(username=request.user)
    getdata=Posts.objects.filter(user_id=userid.id)

    otherusers=User.objects.filter(~Q(username=request.user))
    
    data={
        'data':getdata,
        'users':otherusers
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
    

    data=Posts.objects.get(id=id,user_id=request.user.id).delete()
    return redirect(index)

@login_required
def update(request,id):
    
    data=Posts.objects.get(id=id,user_id=request.user.id)
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
        data=Comments(name=request.user,email='email',comment=request.POST['comment'],post_id=Posts.objects.get(id=id),user_id=request.user.id)
        data.save()
    
    return redirect(read,id=id)

@login_required
def usersprofile(request,username):
    userdata=User.objects.get(username=username)
    data=Posts.objects.filter(user_id=userdata.id)
    return render(request,'users.html',{'data':data})

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

def userregister(request):
    if request.method=='POST':
        username=request.POST['username']
        data=User.objects.all()
       
        for i in data:
            if username==i.username:
                username=None
            

        if username is None:
            
            return HttpResponse(' bu adi istifade ede bilmezsiniz var')
        
        else:
            if request.POST['password']==request.POST['passagain']:
                data=User(username=username,password=request.POST['password'])
                data.save()
                return redirect(userlogin)
            
            else:
                return HttpResponse('parollar beraber deyil')
           
            
    return render(request,'register.html')
# Create your views here.
