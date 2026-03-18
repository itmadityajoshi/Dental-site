from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Doctors(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor_profile')
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)
    specialization = models.CharField(max_length=50, choices=[
        ('general', 'General'),
        ('orthodontis', 'Orthodontis'),
        ('surgeon', 'Surgeon'),
        ('pediatric','Pediatric'),
        ('periodontist', 'Periodontist'),
    ])
    bio = models.TextField(blank=True)
    years_of_experience  = models.PositiveIntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    profile_photo = models.ImageField(upload_to='doctors/photo', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.user.username} ({self.specialization})"


#working hours shift

class WorkingHours(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    doctors = models.ForeignKey(Doctors,on_delete=models.CASCADE, related_name='working_hours')
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = [('doctors', 'day')]

    def __str__(self):
        return f"{self.doctors.user.username} - {self.day}({self.start_time} to {self.end_time})"