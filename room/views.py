# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Booking
from .forms import NewBooking
from django.contrib import messages
# Create your views here.


def index(request):

    rooms = Room.objects.all()
    return render(request, 'layout.html', {'rooms': rooms})


def detail(request, room_id):
    return HttpResponse("estas en la sala %s." % room_id)


def reserva(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = NewBooking(request.POST)
        if form.is_valid():
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']
            if start_time:
                if start_time < end_time:
                    date_depature = dates(end_time, request.POST['start'])
                    date_entry = dates(start_time, request.POST['start'])
                    if Booking.objects.filter(room=room, start__gte=date_entry, end__lte=date_depature).exists():
                        form.add_error(None, "Hay una reserva en ese tramo horario")
                        return render(request, 'reservate.html', {'room': room, 'form': form})
                    variance = date_depature - date_entry
                    r = Booking(title=request.POST['title'], start=date_entry, end=date_depature, start_time=start_time, end_time=end_time, room=room, user=request.user)
            else:
                r = Booking(title=request.POST['title'], start=request.POST['start'], end=request.POST['start'], room=room, user=request.user)

            r.save()

            return HttpResponseRedirect('/')

    else:
        form = NewBooking()

    return render(request, 'reservate.html', {'room': room, 'form': form})


def dates(hours, day):
    hours += ":00"
    day = day + " " + hours
    return datetime.strptime(day, "%Y-%m-%d %H:%M:%S")

