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
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:   
            return redirect("home")  
    else:
        return render(request, "secondpage.html")

def second(request):
    return render(request, "secondpage.html")

def inventory(request):
    return render(request, "inventory.html")

def logout_user(request):
    pass
    
