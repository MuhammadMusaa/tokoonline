from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

 # post save = unk ngesave entah itu ketika diupdate atau di add
 # @receiver adalah decorator(fungsi yg ada diatas class adalah decoator)
 # instance = ia adalah objek 
 # crated = unk membuat
 # **kwargs= unk menambahkan kyword nama="musa"