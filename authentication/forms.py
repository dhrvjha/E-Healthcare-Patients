""""forms for creating and updating user info"""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class patientsRegisterForm(UserCreationForm):
    """Register user and update patients in signal"""

    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password1", "password2"]


class patientsUpdateForm(UserChangeForm):
    """Update user and update patients in signal"""

    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
