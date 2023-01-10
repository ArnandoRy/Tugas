from tkinter import Widget
from django import forms
from django.forms import ModelForm
from dashboard.models import Barang, Data, asia
from django import forms

class FormBarang(ModelForm):
    class Meta  :
        model=Barang
        fields='__all__'
class FormData(ModelForm):
    class Meta  :
        model=Data
        fields='__all__'
class FormData(ModelForm):
    class Meta  :
        model=asia
        fields='__all__'

Widget = {
    'kodebrg' : forms.TextInput({'class':'form-control'}),
    'nama' : forms.TextInput({'class':'form-control'}),
    'stok' : forms.NumberInput({'class':'form-control'}),
    'harga' : forms.NumberInput({'class':'form-control'}),
    'link_gbr' : forms.TextInput({'class':'form-control'}),
    'jenis_id' : forms.Select({'class':'form-control'}),
}        