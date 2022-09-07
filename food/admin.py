from django import forms
from django.contrib import admin
from .models import Booking


# add Booking model to admin panel
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
