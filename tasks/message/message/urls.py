
from django.contrib import admin
from django.urls import path
from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',loginuser),
    path('logout/',logoutuser),
    path('',index),
    path('message/<id>',message),
    path('message/<id>/delete/<messageid>',deletemessage)

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
