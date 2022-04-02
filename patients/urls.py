from django.urls import path

from patients.views import PatientsHomeView, testPatientModel

urlpatterns = [
    path("", PatientsHomeView.as_view(), name="patientHome"),
    path("test/", testPatientModel, name="test_model"),
]
