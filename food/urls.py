from django.urls import path
from . import views, models


urlpatterns = [
    path('', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('bookings', views.bookings, name="bookings"),
]
