"""Views of patient"""


from django import http
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Patients


@login_required
def PatientHomeView(request):
    """First view of patient after login"""
    return render(request, "patients/main.html")


@login_required
def PatientDetailsView(request):
    """Patient detail info view"""
    try:
        patient = Patients.objects.get(user=request.user)
    except Patients.DoesNotExist:
        return http.HttpResponseNotFound
    context = {}
    for key, value in patient.__dict__.items():
        if key != "user":
            context[key] = value
    for key, value in patient.user.__dict__.items():
        context[key] = value
    return render(
        request=request, template_name="patients/detail.html", context=context
    )


def testPatientModel(request):
    """test view to test ML model on different sets of input"""
    return render(request, "patients/test_model.html")
