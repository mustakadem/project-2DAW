from django.shortcuts import render
from django.http import HttpResponse, Http404
from room.models import Reservation, Room


def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})


def search(request):
    # import pdb; pdb.set_trace()
    dates = {
        'outing': request.POST['outing'],
        'entrance': request.POST['entrance']
    }
    rooms = Room.objects.exclude(reservation__date_entry__lte=request.POST['entrance'], reservation__date_departure__gte=request.POST['outing'])
    return render(request, 'search.html', {'dates': dates, 'rooms': rooms})