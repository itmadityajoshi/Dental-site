from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('patient','patient'),
        ('doctor','doctor'),
        ('admin', 'admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')


    def __str__(self):
        return f"{self.username} ({self.role})"