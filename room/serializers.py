
from rest_framework import serializers
from .models import Booking, Room


class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True, source='booking_set')

    class Meta:
        model = Room
        fields = '__all__'





