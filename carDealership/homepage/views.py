from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout #used for logging in and out of user accounts
from django.contrib import messages                 #This allows messages to pop up
from .forms import SignUpForm                       #On the forms.py file(.forms) we use the class SignUpForm 
from .models import employees                       #This will get the info from the employees table in sql

# All below is added
def home(request):
    #check to see if user is logged in
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=email, password=password)     #The username will also be the email
        if user is not None:
            login(request,user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error")
            return redirect("home")  
    else:
        return render(request, "firstpage.html", {})

def second(request):
    return render(request, "secondpage.html")

def inventory(request):
    return render(request, "inventory.html")

def employees_list(request):
    employees_view = employees.objects.all()
    return render(request, "employees.html", {"employees_view":employees_view} )

def logout_user(request):
    logout(request)             #Uses the logout function from the top
    messages.success(request, "You have been logged out!")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)             #Whenever the form is filled out send to the SignUpForm Class
        if form.is_valid():                         #Django will check if the info entered is valued
            form.save()                             #Will save if valid
            #Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)       #passed as password since password1 was renamed to password
            login(request, user)                    #logs in users
            messages.success(request, "You have successgully registered")
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form":form})
    
    return render(request, "register.html", {"form":form})
