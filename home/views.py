from django.shortcuts import render
from django.http import HttpResponse, Http404
from room.models import Booking, Room
from django.http import JsonResponse


def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})


def search(request):
    # import pdb; pdb.set_trace()
    search = {
        'date': request.POST['date'],
        'hours': request.POST['hours']
    }

    if search['hours']:
        rooms = Room.objects.exclude(booking__date_entry=search['date'], booking__hours=search['hours'])
    else:
        rooms = Room.objects.exclude(booking__date_entry=search['date'], booking__date_departure=search['date'])

    return render(request, 'search.html', {'dates': search, 'rooms': rooms})


def calendar(request):
    events = Booking.objects.all()
    return JsonResponse(events, safe=False)