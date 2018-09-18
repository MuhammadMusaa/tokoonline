from django.urls import path
from api.kategori.view import KategoriList
from django.conf.urls import url

urlpatterns = [
	url(r'^', KategoriList.as_view(), name='kategori-list')
]