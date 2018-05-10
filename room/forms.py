from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Booking
from datetime import datetime, date
import pytz


class NewBooking(ModelForm):

    def clean_start(self):
        data = self.cleaned_data['start']
        if data < pytz.UTC.localize(datetime.today()):
            raise ValidationError('Fecha invalida')
        return data

    class Meta:
        model = Booking
        fields = ('title', 'start', 'start_time', 'end_time')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start': forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
        }
