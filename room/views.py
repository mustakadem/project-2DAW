# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import Room

# Create your views here.


def index(request):

    rooms = Room.objects.all()
    return render(request, 'layout.html', {'rooms': rooms})


def detail(request, room_id):
    return HttpResponse("estas en la sala %s." % room_id)


def reserva(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    return HttpResponse('Estas reservando la sala %s.' % room_id)