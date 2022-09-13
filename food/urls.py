from django.urls import path
from . import views, models


urlpatterns = [
    path('', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('bookings', views.add_booking, name="bookings"),
]
