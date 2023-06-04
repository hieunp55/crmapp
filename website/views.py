"""_summary_
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    records = Record.objects.all()
    return render(request, 'home.html', {'records': records})


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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You have successfully registered! Welcome!")
            return redirect('home')

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def view_record(request, pk):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_
    """
    if request.user.is_authenticated:
        # Look Up Records
        record = Record.objects.get(id=pk)

        return render(request, 'record.html', {'record': record})

    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('login')


def delete_record(request, pk):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record is Deleted Successfully!...")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to do that action.")
        return redirect('login')


def add_record(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, "Record is Added...")
            return redirect('home')

        return render(request, 'add_record.html', {'form': form})

    messages.success(request, 'You must logged in!')
    return redirect('login')


def update_record(request, pk):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_
    """
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)

        if form.is_valid():
            form.save()
            messages.success(request, "Record has been Updated")
            return redirect('home')

        return render(request, "update_record.html", {'form': form})

    messages.success(request, 'You must logged in!')
    return redirect('login')
