from rest_framework import serializers
from .models import Booking


class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('start', 'end', 'title', 'start_time', 'end_time', 'user', 'room')