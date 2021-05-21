from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import os

from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('add/',add),
    path('delete/<id>',delete),
    path('update/<id>',update),
    path('todo/<id>',todo),


    
    
] 
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

