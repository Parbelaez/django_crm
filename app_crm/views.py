from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Record

# Create your views here.
def home(request):
    # Get all the records in the table and pass it to the records variable
    records = Record.objects.all()
    # Check to see if logging in
    if request.method == 'POST':
        # Get the values from the form
        username = request.POST['username']
        # Due to a reported bug on Djange, the get method is used to get
        # the value of a key from a dictionary... in this case, the password
        password = request.POST.get('password')
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
            messages.success(request,
                                ('Error logging in - please try again...'))
            # Redirect the user to the login page
            return redirect('home')
    # If not logging in
    else:
        # Render the home page
        return render(request, 'home.html', {'records':records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save the user
            form.save()
            # Get the values from the form, authenticate and login the user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            internet_provider = form.cleaned_data['internet_provider']
            internet_speed = form.cleaned_data['internet_speed']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, 
                                first_name=first_name, last_name=last_name,
                                email=email, address=address, city=city,
                                state=state, zipcode=zipcode,
                                internet_provider=internet_provider,
                                internet_speed=internet_speed,
                                password=raw_password)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            # Send a message to the user
            messages.success(request, 'You have registered...')
            # Redirect the user to the home page
            return redirect('home')
    else:
        # This else statement is needed to render the form for the first time
        # when the user clicks on the register link... don't get confused by the
        # fact that the if statement above is the one registering the user
        form = RegisterForm()
        return render(request, 'register.html', {'form':form, 'title':'Register'})
    
    return render(request, 'register.html', {'form':form, 'title':'Register'})

def customer_record(request, user_id):
    if request.user.is_authenticated:
        # Get the record for the user
        customer_record = Record.objects.get(id=user_id)
        # Render the record page
        return render(request, 
                        'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, ('Please login to view the records...'))
        return redirect('home')

def delete_record(request, user_id):
    if request.user.is_authenticated:
        # Get the record for the user
        customer_record = Record.objects.get(id=user_id)
        # Delete the record
        customer_record.delete()
        # Send a message to the user
        messages.success(request, ('Record has been deleted...'))
        # Redirect the user to the home page
        return redirect('home')
    else:
        messages.success(request, ('Please login to delete records...'))
        return redirect('home')
    
def add_record(request, user_id):
    if request.user.is_authenticated:
        
