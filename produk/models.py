from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)

class Produk(models.Model):
    name = models.CharField(max_length=30)
    merk = models.CharField(max_length=30, blank=True, null=True)
    gambar = models.ImageField(max_length=125, blank=True, null=True)
    harga = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.IntegerField(default=0)
    kategori = models.ForeignKey('Kategori', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    no_hp = models.CharField(max_length=15, null=True)
    alamat = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    catatan = models.TextField(null=True, blank=True)
    ongkir = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(
        choices=(
            ('checkout', 'Checkout'),
            ('paid', 'Terbayar'),
            ('delivered', 'Terkirim'),
        ),
        default='checkout',
        max_length=10,
    )

    def __str__(self):
        return str(self.pk)

class OrderDetail(models.Model):
    order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    produk = models.ForeignKey('Produk', on_delete=models.CASCADE,)
    harga = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=15, decimal_places=2) 

    

    