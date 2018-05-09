from django import forms
from django.forms import ModelForm
from .models import Booking


class NewBooking(ModelForm):
    class Meta:
        model = Booking
        fields = ('title', 'start', 'hours',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start': forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hours': forms.DateTimeInput(attrs={'type': 'time', 'class': 'form-control'}),

        }

