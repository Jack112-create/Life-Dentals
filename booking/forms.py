from django.forms import ModelForm
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ['treatments', 'booking_time', 'booking_date']
        widgets = {
            'booking_date': DateInput()
        }