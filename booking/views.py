from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib import messages

def booking(request):
    user = request.user
    print(user)
    
    form = BookingForm()
    

    if request.method == 'POST':
        form = BookingForm(request.POST)

        selected_time = request.POST['booking_time']
        selected_date = request.POST['booking_date']

        booked_slots = Booking.objects.filter(booking_time=selected_time)
        booked_dates = Booking.objects.filter(booking_date=selected_date)
        print(booked_dates)
        
        if len(booked_dates) > 0:
            for slot in booked_dates:
                if slot.booking_time == selected_time:
                    print('Cannot book that time!')
                    messages.error(request, 'Cannot book that time!')
                    context = {
                        'form': form
                    }
                    return render(request, 'booking/booking.html', context)

                else:
                    if form.is_valid():
                        booking = form.save(commit=False)
                        booking.user = request.user
                        booking.save()
                        print('Booking confirmed')
        else:
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                print('Booking confirmed')
        

        # if len(bookings_dates) == 0:
            
        #     if form.is_valid():
        #         booking = form.save(commit=False)
        #         booking.user = request.user
        #         booking.save()
        #         print('Booking confirmed')
        # else:
        #     print('Cannot book that time!')

    context = {
        'form': form
    }
    return render(request, 'booking/booking.html', context)
