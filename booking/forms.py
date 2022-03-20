from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ['treatments', 'booking_time', 'booking_date']