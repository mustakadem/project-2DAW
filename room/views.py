# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Booking
from .forms import NewBooking
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
            date_entry = request.POST['date_entry']
            if request.POST['hours']:
                hours = request.POST['hours']
                r = Booking(date_entry=date_entry, hours=hours, room=room, user=request.user)
            else:
                r = Booking(date_entry=date_entry, date_departure=date_entry, room=room, user=request.user)

            r.save()

            return HttpResponseRedirect('/')

    else:
        form = NewBooking()

    return render(request, 'reservate.html', {'room': room, 'form': form})


