from django.urls import path
from api.order.view import OrderList, OrderDetail
from django.conf.urls import url

urlpatterns = [
	path(r'', OrderList.as_view(), name='kategori-list'),
	path(r'<pk>', OrderDetail.as_view(), name='kategori-detail'),
]