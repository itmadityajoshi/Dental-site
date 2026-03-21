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

        def __int__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            #only show available doctors
            self.fields['doctors'].queryset = Doctors.objects.filter(is_available=True)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.add_input(Submit('submit','Book Appointment'))


class UpdateAppointmentStatusForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['status','notes']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit','Update Status'))
    

            