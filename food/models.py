from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model for the restaurants 20 tables, max online booking 8 guests

class Bookings(models.Model):
    booking_guests = models.IntegerField()
    booking_time = models.DateTimeField()
    guest_email = models.EmailField()
    guest_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    allergies = models.TextField(max_length=200)
    number_of_tables = models.IntegerField()

    def __str__(self):
        return f'Booking for {self.booking_guests} guests at {self.booking_time}'
