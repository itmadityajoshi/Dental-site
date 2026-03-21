from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from .forms import BookAppointmentForm, UpdateAppointmentStatusForm
from patients.models import Patient
from doctors.models import Doctors

# Create your views here.

@login_required
def book_apppointment_view(req):
    try:
        patient = req.user.patient_profile
    except Patient.DoesNotExist:
        messages.error(req, 'Please complete your patient profile first.')
        return redirect('patient_profile')
    
    if req.method == 'POST':
        form = BookAppointmentForm(req.Post)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            try:
                appointment.save()
                messages.success(req, 'Appointment booked successfylly!')
                return redirect('patient_appointments')
            except Exception:
                messages.error(req, 'That time slot is already booked. Please choose another.')

        else:
            form = BookAppointmentForm()

        context = {'form': form}
        return render(req, 'appointments/book.html', context)
    

@login_required
def patient_appointments_view(req):
    try:
        patient = req.user.patient_profile
    except Patient.DoesNotExist:
        return redirect('patient_profile')
    
    appointment = Appointment.objects.filter(
        patient=patient
    ). order_by('date','time_slot')

    context = {'appointment': appointment}
    return render(req, 'appointments/patient_appointment.html', context)


@login_required
def doctor_appointment_view(req):
    try:
        doctor = req.user.doctor_profile
    except Doctors.DoesNotExist:
        return redirect('doctor_profile')
    
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date','time_slot')
    context = {
        'appointments': appointments
    }

    return render(req, 'appointments/doctor_appointments.html', context)


@login_required
def update_appointment_view(req, appointment_id):
    appointment = get_object_or_404

    
