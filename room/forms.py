from django import forms
from .models import Reservation


class NewBooking(forms.ModelForm):
    class Meta:
        model= Reservation
        fields = [
            'name',
            'surnames',
            'movil',
        ]

        labels ={
            'name': 'Name',
            'surnames': 'Surnames',
            'movil': 'Movil',
        }

        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surnames': forms.TextInput(attrs={'class': 'form-control'}),
            'movil': forms.NumberInput(attrs={'class': 'form-control'}),
        }
