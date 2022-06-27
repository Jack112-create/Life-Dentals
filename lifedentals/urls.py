from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic.urls')),

    path('treatments/', include('treatments.urls')),
    path('booking/', include('booking.urls')),
    path('accounts/', include('users.urls')),
    path('contact/', include('contact.urls')),
]
