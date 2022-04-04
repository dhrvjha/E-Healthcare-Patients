from email.policy import default
from xml.dom import UserDataHandler
from django.db import models
from django.contrib.auth.models import patients




class Profile(models.Model):
    patients = models.OneToOneField(patients, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    

