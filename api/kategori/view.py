from rest_framework import generics
from produk.models import Kategori, Produk
from api.kategori.serializer import KategoriSerializer

class KategoriList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = KategoriSerializer

 # ListCreateAPIView unk get