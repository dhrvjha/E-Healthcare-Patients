from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class PatientsHomeView(View):
    def get(self, request):
        return render(request, "patients/main.html")


def testPatientModel(request):
    return render(request, "patients/test_model.html")
