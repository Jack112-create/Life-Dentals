from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages


def loginUser(request):
    """
    Authenticate the user and then login the user
    """

    page = 'login'

    if request.user.is_authenticated:
        return redirect('booking')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('booking')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {
        'page': page
    }

    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    """
    Logs a user out
    """

    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('login')


def registerUser(request):
    """
    Register a user from form inputs
    Login a user once form is valid
    """

    page = 'register'
    form = CustomUserCreationForm()

    users = User.objects.all()

    if request.method == 'POST':
        try:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()

                messages.success(request, 'User account was created!')
                login(request, user)
                return redirect('booking')

            else:
                messages.error(
                    request, 'An error has occurred during registration')
        except:
            messages.error(
                request, """An error has occurred during registration.
                The username you have chosen already exists.""")

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
