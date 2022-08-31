from django.urls import path
from . import views


urlpatterns = [
    path("", views.BookingList.as_view(), name="home"),
]
