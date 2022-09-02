from django.shortcuts import render
from django.views import generic
from .models import Booking


# view the form for bookings
# class BookingList(generic.ListView):
#    model = Booking

#        template_name = "index.html"

# BookingList is missing a QuerySet. Define BookingList.model, BookingList.queryset, or override BookingList.get_queryset().


#    if request.method == 'POST':
#        form = Booking(request.POST)
#        if form.is_valid():
#           form.save()
#    else:
#        form = Booking()

#    Return render (request, "index.html", {'form':form})
