from django.db import models

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