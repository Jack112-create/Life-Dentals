from django.db import models


class Treatment(models.Model):
    treatment = models.CharField(max_length=200, primary_key=True)
    description = models.TextField(max_length=500, default="")
    price = models.IntegerField()
    duration = models.CharField(max_length=200)

    def __str__(self):
        return str(self.treatment)
