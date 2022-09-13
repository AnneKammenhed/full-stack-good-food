from django.contrib import admin
from .models import Booking, Menu


# add Guest and Booking models to admin panel
@admin.register(Booking, Menu)
class BookingMenuAdmin(admin.ModelAdmin):
    pass
