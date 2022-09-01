from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm
from .models import Booking


# view the form for bookings
class BookingList(generic.ListView):
    form = Booking
    template_name = "index.html"



#    if request.method == 'POST':
#        form = Booking(request.POST)
#        if form.is_valid():
#           form.save()
#    else:
#        form = Booking()

#    Return render (request, "index.html", {'form':form})
