from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def index(request):
    data=User.objects.all()
    return render(request,'index.html',{'data':data})

def add(request):
    if request.method=='POST':
        u=User(name=request.POST['name'])
        u.save()
    return redirect(index)

def read(request,id):

    data=User.objects.get(id=id)
    
    return render(request,'read.html',{'data':data})

def update(request,id):

    data=User.objects.get(id=id)

    if request.method=='POST':
        u=User.objects.get(id=id)
        u.name=request.POST['name']
        u.save()
        return redirect(index)
    
    return render(request,'update.html',{'data':data})

def delete(request,id):
    
    data=User.objects.get(id=id).delete()
        
    return redirect(index)


def addimage(request):
    dataimg=User.objects.all()
    images=Images.objects.all()
    if request.method=='POST':
        data=Images(name='sekil',user_id_id=int(request.POST['img']))
        data.save()
        return redirect(addimage)

    
    return render(request,'images.html',{'data':dataimg,'data2':images})
