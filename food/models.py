from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
# Model for the restaurants 20 tables, max online booking 8 guests

STATUS = ((0, "Draft"), (1, "Confirmed"))

class Booking(models.Model):
    number_of_guests = models.IntegerField()
    booking_time = models.DateTimeField(auto_now=True)
    guest_email = models.EmailField()
    guest_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")
    allergies = models.TextField(max_length=100)

    def __str__(self):
        return f'Booking {self.number_of_guests} guests at {self.booking_time}'
