from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import CustomUser

class RegistrForm(UserCreationForm):
    email = forms.EmailField(required=False)
    role = forms.ChoiceField(choices=[
        ('patinet','Patient'),
        ('doctor','Doctor'),
    ])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1','password2']


class LoginForm(AuthenticationForm):
    pass