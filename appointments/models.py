from django.db import models

# Create your models here.
from accounts.models import CustomUser
from doctors.models import Doctors
from patients.models import Patient

class Appointment(models.Model):

    STATUS_CHOICES = [
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    ]


    TIME_SLOTS = [
        ('09:00', '09:00 AM'),
        ('09:30', '09:30 AM'),
        ('10:00', '10:00 AM'),
        ('10:30', '10:30 AM'),
        ('11:00', '11:00 AM'),
        ('11:30', '11:30 AM'),
        ('12:00', '12:00 PM'),
        ('14:00', '02:00 PM'),
        ('14:30', '02:30 PM'),
        ('15:00', '03:00 PM'),
        ('15:30', '03:30 PM'),
        ('16:00', '04:00 PM'),
        ('16:30', '04:30 PM'),
    ]


    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time_slot = models.CharField(max_length=5, choices=TIME_SLOTS)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    reason = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('doctor','date','time_slot')]
        ordering = ['date','time_slot']
    
    def __str__(self):
        return f"{self.patient.user.username} -> Dr. {self.doctor.user.username} on {self.date} at{self.time_slot}"
