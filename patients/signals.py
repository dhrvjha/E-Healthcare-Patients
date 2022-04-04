"""Save patients after User is saved"""


from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Patients


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created):
    if created:
        Patients.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance):
    instance.patients.save()
