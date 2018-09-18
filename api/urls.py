from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('kategori/', include('api.kategori.urls')),
    path('produk/', include('api.produk.urls')),
    path('docs/', include('api.docs.urls')),
]