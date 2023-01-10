from email.policy import default
from enum import auto
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=20)
    ket=models.TextField()
    def __str__(self):
        return self.nama
class Barang(models.Model):
    kodebrg=models.CharField(max_length=8, default="brg")
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return "{}. {}. {}. {}".format(self.kodebrg,self.nama,self.stok, self.harga)
class Data(models.Model):
    
    kelas=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    nim=models.IntegerField()
    jurusan=models.CharField(max_length=50)
    
    
    waktu_posting=models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return "{}. {}. {}. {}".format(self.kelas,self.nama,self.nim, self.jurusan)

class Transaksi(models.Model):
    kodetrans=models.CharField(max_length=10)
    tggltrans=models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField

    def __str__(self):
        return self.kodetrans

class Detailtrans(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrg=models.CharField(max_length=8)  
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()

    def __str__(self):
        return "{}. {}".format(self.kodetrans,self.kodebrg)   

class asia(models.Model):
    nim=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    sks=models.IntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return "{}. {}. {}. {}".format(self.nim,self.nama,self.sks, self.link_gbr)   