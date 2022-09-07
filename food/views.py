from django.shortcuts import render


def home(request):
    name = "Anne"
    return render(
        request, 
        'index.html', {
        "name": name,
    },)

def menu(request):
    return render(
        request, 
        'menu.html',)

def bookings(request):
    return render(
        request,
        'bookings.html',)