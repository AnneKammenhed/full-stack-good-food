from django.db import models
from django import forms
from .models import Booking
from django.forms import ModelForm


# a form for the Booking model
class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
