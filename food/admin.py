from django.contrib import admin
from .models import Guest


# add Guest and Booking models to admin panel
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass
