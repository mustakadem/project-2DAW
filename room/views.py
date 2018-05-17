# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, generics
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from room.serializers import BookingSerializer, RoomSerializer
from .models import Room, Booking
from .forms import NewBooking


@login_required
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
                        form.add_error(None, "Hay una reserva en ese tramo horario en esta sala")
                        return render(request, 'reservate.html', {'room': room, 'form': form})
                    variance = date_depature - date_entry
                    r = Booking(title=request.POST['title'], start=date_entry, end=date_depature, start_time=start_time,
                                end_time=end_time, room=room, user=request.user)
                    r.save()
                    return HttpResponseRedirect('/')
            else:
                r = Booking(title=request.POST['title'], start=request.POST['start'], end=request.POST['start'],
                            room=room, user=request.user)
                r.save()
                return HttpResponseRedirect('/')

    else:
        form = NewBooking()

    return render(request, 'reservate.html', {'room': room, 'form': form})


def dates(hours, day):
    hours += ":00"
    day = day + " " + hours
    return datetime.strptime(day, "%Y-%m-%d %H:%M:%S")


@permission_classes((permissions.AllowAny,))
class EventsList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@permission_classes((permissions.AllowAny,))
class EventsDetail(APIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class RoomDetail(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def set_booking(self, request, pk=None):
        room = self.get_object()
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(room=room)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)