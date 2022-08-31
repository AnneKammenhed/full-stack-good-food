from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
# Model for the restaurants 20 tables, max online booking 8 guests

class Booking(models.Model):
    number_of_guests = models.IntegerField()

    date_from = models.DateTimeField(
        verbose_name='From',
        blank=True, null=True,
    )

    date_until = models.DateTimeField(
        verbose_name='Until',
        blank=True, null=True,
    )

    creation_date = models.DateTimeField(
        verbose_name='Creation date',
        default=timezone.now(),
    )

    booking_id = models.CharField(
        max_length=100,
        verbose_name='Booking ID',
        blank=True,
    )
    
    guest_email = models.EmailField(
        verbose_name='Email', 
        blank=True,
    )
    
    phone = models.CharField(
        verbose_name='Phone',
        max_length=250,
        blank=True,
    )

    guest_name = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="booking",
    )
    
    allergies = models.TextField(
        max_length=100, 
        verbose_name='allergies',
        blank=True,
    )

#    booking_status = models.ForeignKey(
#        'booking.BookingStatus',
#        verbose_name='Booking status',
#        blank=True, null=True,
#        on_delete=models.CASCADE, related_name="booking",
#    )

    time_period = models.PositiveIntegerField(
        verbose_name='Time period',
        blank=True, null=True,
    )

#    time_unit = models.CharField(
#        verbose_name= 'Time unit',
#        default=getattr(settings, 'BOOKING_TIME_INTERVAL', ''),
#        max_length=64,
#        blank=True,
#    )

    total = models.DecimalField(
        max_digits=36,
        decimal_places=2,
        verbose_name= 'Total',
        blank=True, null=True,
    )

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return f'{self.number_of_guests} guests at {self.date_from} to {self.date_until}'
