from django import forms
from crispy_forms.helper import FormHelper
from crispy_form.layout import Submit
from .models import Appointment
from doctors.models import Doctors


class BookAppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['doctors','date','time_slot','reason']
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'}),
        }

        def __int__(self):
            