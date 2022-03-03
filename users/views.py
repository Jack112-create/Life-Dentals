from django.shortcuts import render

def loginUser(request):

    return render(request, 'users/login_register.html')