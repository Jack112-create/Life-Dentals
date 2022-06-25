from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name="booking"),
    path('create-booking/', views.createBooking, name='create-booking'),
    path('create-booking/htmx/', views.createBookinghtmx, name='create-booking-htmx'),
    path('edit-booking/', views.editBooking, name='edit-booking'),
    path('edit-booking/htmx/', views.editBookinghtmx, name='edit-booking-htmx'),
    path('delete-booking', views.deleteBooking, name='delete-booking'),
]