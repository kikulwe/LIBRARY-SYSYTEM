from django.forms import ModelForm
from django import forms

from auth_app.models import Student

class UserForm(ModelForm):
    class Meta:
        fields=('username', 'reg_no', 'email', 'password')
        model = Student
        widgets = {
            "password": forms.PasswordInput(attrs={'autocomplete': '0ff', 'data-toggle': 'password'}),
        }