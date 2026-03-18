from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    role = forms.ChoiceField(choices=[
        ('patient','Patient'),
        ('doctor','Doctor'),
    ])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1','password2']
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']  # ← explicitly save role
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    pass