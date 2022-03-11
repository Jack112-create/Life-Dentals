from django.shortcuts import render


def home(request):
    """
    Renders the homepage template
    """
    return render(request, 'clinic/homepage.html')
