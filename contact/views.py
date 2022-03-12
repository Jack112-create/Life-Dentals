from django.shortcuts import render

def contact(request):
    """
    Renders contact page
    """
    return render(request, 'contact/contact.html')
