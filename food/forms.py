from django.forms import ModelForm
from .models import Booking


# a form for the Booking model
class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
