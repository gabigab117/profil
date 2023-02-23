from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from profil import settings


# pour rajouter des champs on passe par l'héritage de AbstractUser normalement.
# pourquoi utiliser un modele avec OneToOne ?
class CustomUser(AbstractUser):
    pass


# Dans le cas où je veux différentes données pour différents types d'utilisateurs. Ex un client, un vendeur
class Profile(models.Model):
    # on ne met pas directement la class mais on passe par le fichier de settings
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# relier la fonction post_save_receiver à l'émetteur AUTHUSERMODEL
post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
# qd je crée une instance de CustomUser la fonction post_save_receiver est exécutée
