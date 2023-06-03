"""_summary_
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Return immidiately if not POST method
    return render(request, 'home.html', {})


def login_user(request):
    """_summary_

    Args:
        request (_type_): _description_
    """
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')

        messages.success(
            request, "There was an error logging in, Please try again!")
        return redirect('login')
    # Return immidiately if not POST method
    return render(request, 'login.html', {})


def logout_user(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    logout(request)
    messages.success(request, "You have been logged out ...")
    return redirect('home')


def register_user(request):
    """_summary_
    """
    return render(request, 'login.html', {})
