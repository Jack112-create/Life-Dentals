from django.db import models
from cloudinary.models import CloudinaryField

class Treatment(models.Model):
    treatment = models.CharField(max_length=200, primary_key=True)
    description = models.TextField(max_length=500, default="")
    price = models.IntegerField()
    duration = models.CharField(max_length=200)
    treatment_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.treatment)
