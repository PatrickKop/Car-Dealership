from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout #used for logging in and out of user accounts
from django.contrib import messages                 #This allows messages to pop up

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

def logout_user(request):
    logout(request)             #Uses the logout function from the top
    messages.success(request, "You have been logged out!")
    return redirect("home")


def register_user(request):
    return render(request, "register.html", {})
