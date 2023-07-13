from django.forms import ModelForm
from django import forms

from auth_app.models import User

class UserForm(ModelForm):
    class Meta:
        fields = ('username', 'email', 'password')
        model = User 
        widgets = {
            "password": forms.PasswordInput(attrs={'autocomplete': 'off','data-toggle': 'password'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username']:
            self.fields[fieldname].help_text = None

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'