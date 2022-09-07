from django.contrib import admin
from .models import Guest, Booking


# add Guest and Booking models to admin panel
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    
    list_display = ('guest_name', 'guest_email', 'guest_phone')
    search_fields = ['guest_name', 'guest_email', 'guest_phone']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
