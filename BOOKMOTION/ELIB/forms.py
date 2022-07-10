from django import forms
from django.contrib.auth.models import User
from . import models

class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first-name','last-name','username','password']
