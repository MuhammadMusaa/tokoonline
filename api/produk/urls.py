from django.urls import path
from api.produk.view import ProdukList
from django.conf.urls import url

urlpatterns = [
	url(r'^', ProdukList.as_view(), name='kategori-list')
]