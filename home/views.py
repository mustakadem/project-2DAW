from datetime import datetime

from django.shortcuts import render, redirect
from room.models import Booking, Room
from django.views.decorators.csrf import csrf_exempt
from room.serializers import BookingSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import generics
from django.views.generic import ListView


class Home(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'home.html'


def search(request):
    # import pdb; pdb.set_trace()

    if request.POST['date']:
        search_date = {
            'date': request.POST['date'],
            'hours': request.POST['hours']
        }
        time = search_date['date'] + " 00:00:00"
        time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        if time > datetime.today():
            if search_date['hours']:
                time = search_date['date'] + " " + search_date['hours'] + ":00"
                time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                rooms = Room.objects.exclude(booking__start=time)
            else:
                rooms = Room.objects.exclude(booking__start=search_date['date'], booking__end=search_date['date'])
        else:
            return redirect('home')
    else:
        return redirect('home')

    return render(request, 'home.html', {'date': time.strftime("%d-%m-%Y %H:%M"), 'rooms': rooms})


@csrf_exempt
def form_reservate(request):
    return 'hi'


