from rest_framework import generics, permissions
from produk.models import Order
from api.order.serializer import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions_classes = (permissions.IsAuthenticated)
    # filter_backends = (DjangoFilterBackend,)
    

 # ListCreateAPIView unk get
 # disable = 
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions_classes = (permissions.IsAuthenticated)
