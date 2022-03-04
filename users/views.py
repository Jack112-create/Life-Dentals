from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('booking')

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('booking')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {
        'page': page
    }

    return render(request, 'users/login_register.html', context)
