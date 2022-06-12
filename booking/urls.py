from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name="booking"),
    path('create-booking/', views.createBooking, name='create-booking'),
    path('edit-booking/', views.editBooking, name='edit-booking'),
    path('delete-booking', views.deleteBooking, name='delete-booking')
]