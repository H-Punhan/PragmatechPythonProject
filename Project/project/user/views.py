from django.shortcuts import render,redirect
from .models import *

def index(request):
    data=User.objects.all()
    return render(request,'index.html',{'data':data})

def add(request):
    if request.method=='POST':
        u=User(name='Punhan')
        u.save()
    return redirect(index)

    
    
