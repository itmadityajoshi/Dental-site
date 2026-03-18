from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile')
    phone = models.CharField( max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'FeMale'),
        ('other', 'Other'),
    ], blank=True)
    address = models.CharField(max_length=50)
    dental_history = models.CharField(blank=True)
    profile_photo = models.ImageField(upload_to='patients/photos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patients : {self.user.username}"


