from django.shortcuts import render
from django.http import HttpResponse, Http404
from room.models import Booking, Room
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def calendar(request):
    events = Booking.objects.all()
    data = serializers.serialize('json', events)
    return JsonResponse(data, safe=False)