from django.shortcuts import render
from .models import Booking
from .forms import BookingForm

def booking(request):
    user = request.user
    print(user)
    
    # print(bookings)

    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)

        my_time = 0
        bookings = Booking.objects.filter(booking_time=my_time)
        print(bookings)

        if len(bookings) == 0:
            print(len(bookings))
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
        else:
            print('Cannot book that time!')

    context = {
        'form': form
    }
    return render(request, 'booking/booking.html', context)
