from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Model to book a table

class Booking(models.Model):
    
    booking_id = models.CharField(
        max_length=100,
        verbose_name='Booking ID',
        blank=True,
    )
    number_of_guests = models.IntegerField()

    date = models.DateField(
        verbose_name='Date',
        blank=True, null=True,
    ) 

    time = models.DateTimeField(
        verbose_name='Time',
        blank=True, null=True,
    )

    guest_name = models.CharField(max_length=50)
    
    guest_email = models.EmailField(
        verbose_name='Email', 
        blank=True,
    )
    
    phone = models.CharField(
        verbose_name='Phone',
        max_length=250,
        blank=True,
    )

    allergies = models.TextField(
        max_length=100, 
        verbose_name='allergies',
        blank=True,
    )

    def __str__(self):
        return f'{self.number_of_guests} guests at {self.time}{self.date}'
