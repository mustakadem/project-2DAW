from django import forms
from django.forms import ModelForm
from .models import Reservation


class NewBooking(ModelForm):
    class Meta:
        model = Reservation
        fields = ('date_entry', 'date_departure')
        widgets = {
            'date_entry': forms.DateTimeInput(attrs={'type': 'date'}),
            'date_departure': forms.DateTimeInput(attrs={'type': 'date'})
        }

