from django.urls import path
from api.kategori.view import KategoriList, KategoriDetail
from django.conf.urls import url

urlpatterns = [
	path(r'', KategoriList.as_view(), name='kategori-list'),
	path(r'<pk>', KategoriDetail.as_view(), name='kategori-detail'),
]