from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import patientsRegisterForm, patientsUpdateForm, patientsUpdateForm
from django.contrib.auth.forms import patientsCreationForm
from django.views.generic import View

# Create your views here.


class PatientsHomeView(View):
    def get(self, request):
        return render(request, "patients/main.html")


def testPatientModel(request):
    return render(request, "patients/test_model.html")


def register(request):
    if request.method =='POST':
         form = patientsRegisterForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data.get('firstName','lastName')
            messages.success(request, f'Your account has been created! You are now able to Login ')
            return redirect('login')
    else:
         form = patientsRegisterForm()
    return render(request, 'patients/register.html',{'form': form})

@login_required    
def profile(request):
     if request.method =='POST':
          u_form = patientsUpdateForm(request.POST, instance=request.patients)
          p_form = patientsUpdateForm(request.POST,
          request.FILES, 
          instance= request.user.profile)

          if u_form.is_valid() and p_form.is_valid():
               u_form.save()
               p_form.save()
               messages.success(request, f'Your account has been Updated!')
               return redirect('profile')

     else:
          u_form = patientsUpdateForm(instance=request.patients)
          p_form = patientsUpdateForm(instance=request.patients.profile)   

     context = {
          'u_form' : u_form,
          'p_form' : p_form
     }
     return render (request,'patients/profile.html',context)    
