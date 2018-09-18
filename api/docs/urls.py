from django.urls import path
from api.docs.view import schema_view
from django.conf.urls import url

urlpatterns = [
	url(r'^', schema_view),
	# url(r'^', ProdukList.as_view(), name='Produk-list'),
]