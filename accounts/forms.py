from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Register'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']  # ← explicitly save role
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Login'))  