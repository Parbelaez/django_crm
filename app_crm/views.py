from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        # Get the values from the form
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        # If the user is valid
        if user is not None:
            # Log the user in
            login(request, user)
            # Send a message to the user
            messages.success(request, 'You have been logged in!')
            # Redirect the user to the home page
            return redirect('home')
        # If the user is not valid
        else:
            # Send a message to the user
            messages.success(request, ('Error logging in - please try again...'))
            # Redirect the user to the login page
            return redirect('home')
    # If not logging in
    else:
        # Render the home page
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('home')

