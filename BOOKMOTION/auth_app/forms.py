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

    def __int__(self,*args, **kwargs):
        super(UserForm, self).__int__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'