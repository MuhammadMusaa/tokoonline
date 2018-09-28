from rest_framework import generics, permissions
from produk.models import Kategori, Produk
from api.kategori.serializer import KategoriSerializer

class KategoriList(generics.ListCreateAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly)

 # ListCreateAPIView unk get

class KategoriDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer