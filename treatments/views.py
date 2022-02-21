from django.shortcuts import render


def treatments(request):
    """
    Renders the treatments page
    """
    return render(request, 'treatments/treatments.html')
