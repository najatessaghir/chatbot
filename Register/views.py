from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import AuthForm , Registerform 
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('/')  # Replace 'home' with your home page name
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = Registerform()
    return render(request, 'register/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('/')  # Replace 'home' with your home page name
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthForm()
    return render(request, 'register/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('/')  # Replace 'home' with your home page name

