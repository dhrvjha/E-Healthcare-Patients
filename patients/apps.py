from django.apps import AppConfig

import patients


class PatientsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "patients"
    
    def ready(self) :
        return patients.signals
