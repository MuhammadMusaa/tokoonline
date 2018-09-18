from rest_framework import generics
from produk.models import Kategori, Produk
from api.produk.serializer import ProdukSerializer

class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

 # ListCreateAPIView unk get