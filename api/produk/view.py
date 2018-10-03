from rest_framework import generics, permissions
from produk.models import Produk
from api.produk.serializer import ProdukSerializer

class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

 # ListCreateAPIView unk get
 # disable = 
class ProdukDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)
