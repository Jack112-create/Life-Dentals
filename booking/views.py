from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.contrib import messages
import datetime


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

    today_date = datetime.datetime.now().date()

    bookings = Booking.objects.all()
    print(bookings)
    booked_times = []

    for booking in bookings:
        if booking.booking_date == today_date:
           booked_times.append(booking.booking_time)
    
    print(booked_times)

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
        'form': form,
        'booked_times': booked_times,
        'today_date': today_date
    }

    return render(request, 'booking/create-booking.html', context)


def createBookinghtmx(request):
    if request.htmx:
        form = BookingForm()

        date = request.POST['booking_date']
        print(date)

        today_date = datetime.datetime.now().date()

        treatment = request.POST['treatments']

        bookings = Booking.objects.filter(booking_date=date)
        booked_times = []

        for slot in bookings:
            booked_times.append(slot.booking_time)

        context = {
            'treatment': treatment,
            'times': booked_times,
            'date': date,
            'form': form,
            'today_date': today_date
        }
        return render(request, 'booking/snippet/booking-snippet.html', context)


@login_required(login_url='login')
def editBooking(request):
    user = request.user

    booking = Booking.objects.get(user=user)

    form = BookingForm(instance=booking)

    today_date = datetime.datetime.now().date()

    bookings = Booking.objects.filter(booking_date=booking.booking_date)
    print(bookings)
    booked_times = []

    for times in bookings:
        booked_times.append(times.booking_time)

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
        'form': form,
        'booked_times': booked_times,
        'today_date': today_date
    }

    return render(request, 'booking/edit-booking.html', context)


def editBookinghtmx(request):
    print('request to edit booking htmx')
    if request.htmx:
        print('htmx request was made')
        user = request.user

        booking = Booking.objects.get(user=user)

        form = BookingForm(instance=booking)

        date = request.POST['booking_date']
        print(date)

        today_date = datetime.datetime.now().date()

        treatment = request.POST['treatments']

        bookings = Booking.objects.filter(booking_date=date)
        booked_times = []

        for slot in bookings:
            booked_times.append(slot.booking_time)

        context = {
            'treatment': treatment,
            'times': booked_times,
            'date': date,
            'form': form,
            'today_date': today_date,
            'test': 'testing edit'
        }
        return render(request, 'booking/snippet/edit-booking-htmx.html', context)


@login_required(login_url='login')
def deleteBooking(request):
    user = request.user
    booking = Booking.objects.get(user=user)

    if request.method == 'POST':
        booking.delete()
        return redirect('booking')

    context = {"object": booking}
    return render(request, 'booking/delete-booking.html', context)
