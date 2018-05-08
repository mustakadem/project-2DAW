from django import forms
from django.forms import ModelForm
from .models import Booking


class NewBooking(ModelForm):
    class Meta:
        model = Booking
        fields = ('name_event', 'date_entry', 'hours', )
        widgets = {
            'name_event': forms.TextInput(attrs={'class': 'form-control'}),
            'date_entry': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hours': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),

        }

