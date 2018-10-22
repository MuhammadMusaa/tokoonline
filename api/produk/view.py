from rest_framework import generics, permissions
from produk.models import Produk
from api.produk.serializer import ProdukSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('kategori',)

 # ListCreateAPIView unk get
 # disable = 
class ProdukDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)
