from datetime import datetime

from django.shortcuts import render, redirect
from room.models import Booking, Room
from django.views.decorators.csrf import csrf_exempt
from room.serializers import BookingSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import generics


def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms, })


def search(request):
    # import pdb; pdb.set_trace()

    search = {
        'date': request.POST['date'],
        'hours': request.POST['hours']
    }
    if search['date']:
        time = search['date'] + " 00:00:00"
        time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        if time > datetime.today():
            if search['hours']:
                time = search['date'] + " " + search['hours'] + ":00"
                time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                rooms = Room.objects.exclude(booking__start=time)
            else:
                rooms = Room.objects.exclude(booking__start=search['date'], booking__end=search['date'])
        else:
            return redirect('home')
    else:
        return redirect('home')

    return render(request, 'home.html', {'date': time.strftime("%d-%m-%Y %H:%M"), 'rooms': rooms})


@csrf_exempt
def form_reservate(request):
    return 'hi'


