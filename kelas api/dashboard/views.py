from urllib import request
from django.shortcuts import render
from dashboard.forms import FormBarang, FormData
from dashboard.models import Barang, Data, asia

def product(request):
    title =  "product"
    setTitle = {
        'title':title
    }
    return render(request,'product.html',setTitle)

def about(request):
    
    return render(request,'about.html')

def project(request):
    
    return render(request,'project.html')

def contact(request):
    
    return render(request,'contact.html')

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)
   
def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs': barangs,
    }   
    return render(request,'tampil_brg.html',konteks)


def tambah_data(request):
    form=FormData()
    konteks={
        'data':form,
    }
    return render(request,'tambah_data.html',konteks)
      
def Data_Kelas(request):
    kelas=Data.objects.all()

    konteks={
        'kelas': kelas,
    }   
    return render(request,'data_kelas.html',konteks)


def Asia_View(request):
    asias=asia.objects.all()

    konteks={
        'asias': asias,
    }   
    return render(request,'asia.html',konteks)
