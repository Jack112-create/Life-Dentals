from django.shortcuts import render
from .models import Treatment


def treatments(request):
    """
    Renders the treatments page
    """

    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments
    }

    return render(request, 'treatments/treatments.html', context)
