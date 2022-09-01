from django.shortcuts import render
from django.views import generic
from .models import Booking


# view the Bookings
class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = "booking.html"
