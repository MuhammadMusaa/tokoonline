from django.contrib import admin
from produk.models import Produk, Kategori, Order, OrderDetail

# Register your models here.

admin.site.register(Produk)
admin.site.register(Kategori)
admin.site.register(Order)
admin.site.register(OrderDetail)

