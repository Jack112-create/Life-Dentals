from django.db import models
from django.contrib.auth.models import User
from treatments.models import Treatment
from datetime import datetime, date


class Booking(models.Model):

    TREATMENTS_LIST = []

    TIMESLOT_LIST = (
        ('0', '09:00 – 09:30'),
        ('1', '10:00 – 10:30'),
        ('2', '11:00 – 11:30'),
        ('3', '12:00 – 12:30'),
        ('4', '13:00 – 13:30'),
        ('5', '14:00 – 14:30'),
        ('6', '15:00 – 15:30'),
        ('7', '16:00 – 16:30'),
        ('8', '17:00 – 17:30'),
    )

    # Retrieve all instances of Treatment model
    TREATMENT_CHOICES = Treatment.objects.all()

    # Add treatments into tuple so that it can be added to choices parameter below
    for i in range(len(TREATMENT_CHOICES)):
        TREATMENTS_LIST.append((f'{TREATMENT_CHOICES[i].treatment}', TREATMENT_CHOICES[i].treatment))
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    treatments = models.CharField(max_length=15, choices=TREATMENTS_LIST)
    booking_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    booking_time = models.CharField(max_length=50, choices=TIMESLOT_LIST, default=TIMESLOT_LIST[0][1])

    def __str__(self):
        return str(f'{self.user}: booking')
