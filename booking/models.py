from django.db import models
from django.contrib.auth.models import User
from treatments.models import Treatment


class Booking(models.Model):

    TREATMENTS_LIST = []

    # Retrieve all instances of Treatment model
    TREATMENT_CHOICES = Treatment.objects.all()

    # Add treatments into tuple so that it can be added to choices parameter below
    for i in range(len(TREATMENT_CHOICES)):
        TREATMENTS_LIST.append((f'{TREATMENT_CHOICES[i].treatment}', TREATMENT_CHOICES[i].treatment))
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    treatments = models.CharField(max_length=15, choices=TREATMENTS_LIST)

    def __str__(self):
        return str(f'{self.user}: booking')
