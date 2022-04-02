import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Patients(models.Model):
    class PriorityChoices(models.TextChoices):
        EME = "1", "Emergency"
        ADM = "2", "Admit"
        NOR = "3", "Normal"

    id = models.UUIDField(
        default=uuid.uuid4, blank=True, null=False, primary_key=True, db_index=True
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    firstName = models.CharField(max_length=150, blank=False)
    lastName = models.CharField(max_length=150, blank=False)
    age = models.PositiveIntegerField(blank=False)
    priority = models.CharField(
        max_length=2, choices=PriorityChoices.choices, default=PriorityChoices.EME
    )

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def get_absolute_url(self):
        return reverse("patients-RUD", kwargs={"pk": self.id})
