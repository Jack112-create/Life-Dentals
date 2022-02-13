from django.shortcuts import render


def home(request):
    """
    Renders the main base.html template
    """
    return render(request, 'base.html')
