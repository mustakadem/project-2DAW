from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.utils import json

from room.models import Booking, Room
from django.views.decorators.csrf import csrf_exempt
from room.serializers import BookingSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import generics
from django.views.generic import ListView
from room.views import dates


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


@login_required
def reservate_calendar(request):
    response_data = {}
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    if start_time:
        if start_time < end_time:
            date_depature = dates(end_time, request.POST['start'])
            date_entry = dates(start_time, request.POST['start'])
            if request.POST['room'] != 'select':
                room = get_object_or_404(Room, pk=request.POST['room'])
                if Booking.objects.filter(room=room, start__lte=date_entry,
                                          end__gte=date_depature).exists():
                    response_data['error'] = 'La reserva ya existe en este tramo horario'
                else:
                    r = Booking(title=request.POST['title'], start=date_entry, end=date_depature, start_time=start_time,
                                end_time=end_time, room=room, user=request.user)
                    r.save()

                    response_data['result'] = 'Se ha creado la reserva'
            else:
                response_data['error'] = "Debes seleccionar una sala"
        else:
            response_data['error'] = "La hora de salida debe ser mayor a la de entrada"

    else:
        response_data['error'] = 'Debes seleccionar una hora'

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required
def delete_calendar(request, room_id, book_id):

    user_id = request.GET['user']
    response_data = {}
    if Booking.objects.filter(room_id=room_id, id=book_id, user_id=user_id).exists():
        Booking.objects.filter(room_id=room_id, id=book_id, user_id=user_id).delete()
        response_data['result'] = 'Evento Eliminado Correctamente'
    else:
        response_data['error'] = 'El evento no esta asociado a este usuario'

    return HttpResponse(json.dumps(response_data), content_type="application/json")
