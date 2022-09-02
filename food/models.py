from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# values for what days Good Food is open, three seatings:
OPENING_DAYS = (
    (0, "Tuesday"),
    (1, "Wednesday"),
    (2, "Thursday"),
    (3, "Friday"),
    (4, "Saturday"),   
)

SEATING_TIMES = (
    (0, "17.00-18.30"),
    (1, "18.30-20.00"),
    (2, "20.00-21.30"),
)

# online booking allows for a maximum of eight guests
NUMBER_OF_GUESTS = (
    (0, "One guest"),
    (1, "Two guests"),
    (2, "Three guests"),
    (3, "Four guests"),
    (4, "Five guests"),
    (5, "Six guests"),
    (6, "Seven guests"),
    (7, "Eight guests"),
)

# Model to book a table = available times+number of guests+guest details
class Booking(models.Model):
    
    booking_day = models.IntegerField(
        choices=OPENING_DAYS,
        default=0,
    )
    
    booking_time = models.IntegerField(
        choices=SEATING_TIMES,
        default=0,
    )

    number_of_guests = models.IntegerField(
        choices=NUMBER_OF_GUESTS, 
        default=0,
    )

    guest = models.TextField(
        max_length=50, 
        verbose_name='Guest',
        blank=True,
    )
    
    guest_email = models.EmailField(
        verbose_name='Email', 
        blank=True,
    )
    
    allergies = models.TextField(
        max_length=100, 
        verbose_name='Allergies',
        blank=True,
    )

    # class Meta:
    #     ordering = ('booking_day', 'booking_time')
    #     unique_together = ('guest', 'booking_day', 'booking_time')

    def __str__(self):
        return f'{self.guest} for {self.number_of_guests} at {self.booking_day}{self.booking_time}'

    # funtion to show vacant times grouped per day
    # def show_vacancy(available_times):
    #     availability = {}
    #    for vacant in available_times:
    #        vacant_day, vacant_time = vacant[0], vacant[1]
    #        availability[vacant_day] = availability.get(vacant_day, []) + [vacant_time]
    #    return availability
