from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.contrib import messages


@login_required(login_url='login')
def booking(request):
    user = request.user

    try:
        bookings = user.booking
    except:
        print('no bookings')
        bookings = ''

    context = {
        "bookings": bookings
    }

    return render(request, 'booking/booking.html', context)


@login_required(login_url='login')
def createBooking(request):
    user = request.user

    try:
        bookings = Booking.objects.get(user=user)
        return redirect('booking')
    except:
        pass

    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)

        # Get user selected time and date for booking
        selected_time = request.POST['booking_time']
        selected_date = request.POST['booking_date']

        """ Query booking table to find time & date that
        match user selected time and date
        """
        booked_slots = Booking.objects.filter(booking_time=selected_time)
        booked_dates = Booking.objects.filter(booking_date=selected_date)

        # Check if the form data is valid
        if form.is_valid():
            booking = form.save(commit=False)
            # Assign the user with the booking
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking Successful!')
            return redirect('booking')

    context = {
        'form': form
    }

    return render(request, 'booking/create-booking.html', context)


@login_required(login_url='login')
def editBooking(request):
    user = request.user

    booking = Booking.objects.get(user=user)

    form = BookingForm(instance=booking)

    if request.method == 'POST':
        # Get user selected time and date for booking
        selected_time = request.POST['booking_time']
        selected_date = request.POST['booking_date']

        """ Query booking table to find time & date that
        match user selected time and date
        """
        booked_slots = Booking.objects.filter(booking_time=selected_time)
        booked_dates = Booking.objects.filter(booking_date=selected_date)

        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking')

        else:
            messages.error(request, 'Cannot book that time!')

    context = {
        'form': form
    }

    return render(request, 'booking/edit-booking.html', context)


@login_required(login_url='login')
def deleteBooking(request):
    user = request.user
    booking = Booking.objects.get(user=user)

    if request.method == 'POST':
        booking.delete()
        return redirect('booking')

    context = {"object": booking}
    return render(request, 'booking/delete-booking.html', context)
