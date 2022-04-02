from django.urls import path

from patients.views import PatientsHomeView

urlpatterns = [path("", PatientsHomeView.as_view(), name="patientHome"),
    path("test/", )]
