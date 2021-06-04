from django.core.checks import messages
from app.models import Messages
from django.contrib.auth.models import User

from django.db.models import Q

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



@login_required
def index(request):

    users=User.objects.all()

    return render(request,'index.html',{'data':users})

@login_required
def message(request,id):

    if request.method=='POST':
        usermessage=request.POST['message']

        sending=Messages(sender_id=request.user.id,owner_id=id,message=usermessage)
        sending.save()
        return redirect(message,id)
    
    data=Messages.objects.filter(Q(sender=request.user.id,owner=id)|Q(sender=id,owner=request.user.id)).order_by('id')
    data2=User.objects.get(id=id)
    return render(request,'message.html',{'data':data,'userdata':data2})

@login_required
def deletemessage(request,id,messageid):
    data=Messages.objects.get(id=messageid,sender_id=request.user.id).delete()
    
    return redirect(message,id)
def loginuser(request):

    

    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect(index)
            
        else:
            return redirect(loginuser)
            

    return render(request,'login.html')
  
@login_required
def logoutuser(request):
    logout(request)
    return redirect(loginuser)
# Create your views here.
