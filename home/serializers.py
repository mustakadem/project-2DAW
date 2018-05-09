from rest_framework import serializers
from room.models import Booking


class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('start', 'end', 'title', 'hours', 'user', 'room')