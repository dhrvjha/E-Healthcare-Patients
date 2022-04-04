import profile
from pyexpat import model
from django import forms
from django.contrib.auth.models import patients
from django.contrib.auth.forms import patientsCreationForm
from.models import Profile

class patientsRegisterForm(patientsCreationForm):
    email =  forms.EmailField()

    class Meta :
        model = patients
        fields = ['firstName','lastName','email','password1','password2']



class patientsUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta :
        model = patients
        fields = ['username','email']
