from django import forms
from .models import Patient

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['phone','date_of_birth','gender','address','dental_history','profile_photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address' : forms.Textarea(attrs={'rows':3}),
            'dental_history': forms.Textarea(attrs={'rows': 4}),
        }