from django.shortcuts import render
from django.views import generic
from .models import Booking


# Create your views here:
# view to se the Bookings model
class BookingList(generic.ListView):
    model = Booking
    template_name = 'index.html'
