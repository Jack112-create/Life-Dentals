from django.forms import ModelForm
from django import forms
from .models import Booking
from .models import Treatment


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    treatments = forms.ModelChoiceField(queryset=Treatment.objects.all(), empty_label=None)

    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'treatments']
        widgets = {
            'booking_date': DateInput()
        }
