from django.shortcuts import render
from django.views.generic import ListView
from .models import Booking

# Create your views here:
# view to se the Bookings model
class BookingList(ListView):
    model = Booking
