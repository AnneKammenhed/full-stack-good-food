from django.db import models


# Model for the guest contact info
class Guest(models.Model):
    guest_name = models.CharField(
        max_length=25,
        verbose_name='Guest',
        blank=True,
    )

    guest_email = models.EmailField(
        verbose_name='Email', 
        blank=False,
    )

    guest_phone = models.CharField(
        max_length=25,
        verbose_name='Phone',
        blank=True,
    )

    def __str__(self):
        return f'{self.guest_name}'


# Model to book a table = available times+number of guests+guest details
class Booking(models.Model):
    # values for what days Good Food is open, three seatings:
    TUESDAY = 'Tue'
    WEDNESDAY = 'Wed'
    THURSDAY = 'Thu'
    FRIDAY = 'Fri'
    SATURDAY = 'Sat'
    OPENING_DAYS_CHOICES = [
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),   
    ]

    DINNER1 = '17.00-18.30'
    DINNER2 = '18.30-20.00'
    DINNER3 = '20.00-21.30'
    SEATING_TIMES_CHOICES = [
        (DINNER1, '17.00-18.30'),
        (DINNER2, '18.30-20.00'),
        (DINNER3, '20.00-21.30'),
    ]

    # online booking allows for a maximum of eight guests
    ONE = 'One guest'
    TWO = 'Two guests'
    THREE = 'Three guests'
    FOUR = 'Four guests'
    FIVE = 'Five guests'
    SIX = 'Six guests'
    SEVEN = 'Seven guests'
    EIGHT = 'Eight guests'
    NUMBER_OF_GUESTS = [
        (ONE, 'One guest'),
        (TWO, 'Two guests'),
        (THREE, 'Three guests'),
        (FOUR, 'Four guests'),
        (FIVE, 'Five guests'),
        (SIX, 'Six guests'),
        (SEVEN, 'Seven guests'),
        (EIGHT, 'Eight guests'),
    ]

    booking_week = models.IntegerField(
        max(1, 52),
        default=1
    )

    booking_day = models.CharField(
        max_length=10,
        choices=OPENING_DAYS_CHOICES,
        default=TUESDAY,
    )
    
    booking_time = models.CharField(
        max_length=20,
        choices=SEATING_TIMES_CHOICES,
        default=DINNER1,
    )
    
    number_of_guests = models.CharField(
        max_length=20,
        choices=NUMBER_OF_GUESTS, 
        default=TWO,
    )

    allergies = models.TextField(
        max_length=100, 
        verbose_name='Allergies',
        blank=True,
    )

    guest = models.ForeignKey(
        Guest, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
    )

    class Meta:
        ordering = ('booking_week', 'booking_day', 'booking_time')
        unique_together = ('guest', 'booking_day', 'booking_time')

    def __str__(self):
        return f'{self.guest} for {self.number_of_guests} on {self.booking_day} at {self.booking_time}'
