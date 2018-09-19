from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('kategori/', include('api.kategori.urls')),
    path('produk/', include('api.produk.urls')),
    path('docs/', include('api.docs.urls')),
    path('api-token/', views.obtain_auth_token,)
]