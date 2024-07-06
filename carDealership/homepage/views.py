from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout #used for logging in and out of user accounts
from django.contrib import messages                 #This allows messages to pop up
from .forms import SignUpForm, AddEmployeeForm                       #On the forms.py file(.forms) we use the class SignUpForm 
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
    if request.user.is_authenticated:
        employees_view = employees.objects.all()            #Grabs all the records from employees
        return render(request, "employees.html", {"employees_view":employees_view} )
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')


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

def employees_record(request, pk):
    if request.user.is_authenticated:       #This is to make sure the user is logged in before viewing record
        #Look up employee records
        employee_record = employees.objects.get(id=pk)      #Get will only get the object that is called. All will grab all the records
        return render(request, "employeeRecord.html", {"employee_record":employee_record})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')


def delete_employees_record(request, pk):
    if request.user.is_authenticated:
        remove_employee = employees.objects.get(id=pk)
        remove_employee.delete()
        messages.success(request, "Employee record has been deleted successfully")
        return redirect('employees')
        #add confirmation to delete employee
    else:
        messages.success(request, "You must be logged in to do that")
        return redirect('home')
    
def add_employee(request):
    form = AddEmployeeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                add_employee = form.save()
                messages.success(request, "Employee has been added")
                return redirect('home')
        return render(request, "addEmployee.html", {"form":form}) 
    else:
        messages.success(request, "You must be logged in to add employees")
        return redirect('home')     


def update_employees_record(request, pk):
    if request.user.is_authenticated:
        current_record = employees.objects.get(id=pk)
        form = AddEmployeeForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('employees')
        return render(request, "updateEmployeeRecord.html", {"form":form}) 
    else:
        messages.success(request, "You must be logged in to update employees")
        return redirect('home')   


