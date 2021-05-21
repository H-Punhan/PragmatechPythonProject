from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *




def index(request):
    data=Todos.objects.all()
    if request.method=='POST':
        if request.POST['filter']=='veiwers':
            data=Todos.objects.all().order_by('-viewers')
        elif request.POST['filter']=='a-z':
            data=Todos.objects.all().order_by('title')
            print(data[0].title)
       

        return render(request,'index.html',{'data':data})
    return render(request,'index.html',{'data':data})
    
    

def add(request):
    if request.method=='POST':
        data=Todos(title=request.POST['title'],content=request.POST['content'])
        data.save()
        return redirect(index)
    return render(request,'add.html')
    

def delete(request,id):
    
    data=Todos.objects.get(id=id).delete()
    
    return redirect(index)

def update(request,id):
    
    data=Todos.objects.get(id=id)

    if request.method=='POST':
        data.title=request.POST['title']
        data.content=request.POST['content']
        data.save()
        return redirect(index)
    return render(request,'update.html',{'data':data})
   
def todo(request,id):
    chang=Todos.objects.get(id=id)
    chang.viewers=chang.viewers+1
    chang.save()
    data=Todos.objects.get(id=id)

    return render(request,'todo.html',{"data":data})