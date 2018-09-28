from django.urls import path
from api.produk.view import ProdukList, ProdukDetail
from django.conf.urls import url

urlpatterns = [
	path(r'', ProdukList.as_view(), name='kategori-list'),
	path(r'<pk>', ProdukDetail.as_view(), name='kategori-detail'),
]