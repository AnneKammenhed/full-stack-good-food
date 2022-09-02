from django.contrib import admin
from .models import Booking


# add Booking model to admin panel

admin.site.register(Booking)

# list_filter = ('booking_time', 'guest_name')
