from django.contrib import admin

# Register your models here.
from .models import Barang,Transaksi,Detailtrans, Jenis, Data,asia
class kolomBarang(admin.ModelAdmin):
    list_display= ['kodebrg','nama','stok','harga','link_gbr','jenis_id']
    search_fields=['kodebrg','nama']
    list_filter=('jenis_id',)
    list_per_page=5

admin.site.register(Barang, kolomBarang)
admin.site.register(Transaksi)
admin.site.register(Detailtrans)
admin.site.register(Jenis)
admin.site.register(Data)
admin.site.register(asia)