from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import product
from dashboard.views import about
from dashboard.views import project
from dashboard.views import contact, tambah_barang, Barang_View, Data_Kelas, tambah_data, Asia_View
from dashboard.views_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('asia/',asiaViewset)



def home(request):
    title="Home"
    setTitle = {
        'titel':title,
    }
    return render(request,'home.html',setTitle)
def about(request):
   
    
    return render(request,'about.html')

def project(request):
   
    
    return render(request,'project.html')
def contact(request):
   
    
    return render(request,'contact.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('product/',product),
    path('about/', about),
    path('project/', project),
    path('contact/', contact),
    path('addbrg/',tambah_barang),
    path('adddata/',tambah_data),
    path('vbrg/',Barang_View),
    path('vkelas/',Data_Kelas),
    path('vasia/',Asia_View),

    path('api/',include(router.urls)),

]
