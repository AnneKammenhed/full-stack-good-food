from django.contrib import admin
from django import forms
from django.forms import ModelForm
from .models import Booking

# Register your models here:
# add Booking model to our admin panel
class PostAdmin(admin.ModelAdmin):
    form = Booking
