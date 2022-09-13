from django.shortcuts import render
from .forms import BookingForm


def add_booking(request):
    submitted = False
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return HttpResponseRedirect('bookings?submitted=True')
    else:
        booking_form = BookingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'bookings.html', {'form': booking_form, 'submitted': submitted})

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')
