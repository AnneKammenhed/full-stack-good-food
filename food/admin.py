from django.contrib import admin
from .models import Booking, Menu


# add Guest and Booking models to admin panel
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('guest', 'booking_week', 'booking_day', 'booking_time') 
    search_fields = ['guest', 'booking_week', 'booking_day', 'booking_time']
    list_filter = ('guest', 'booking_day')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass
