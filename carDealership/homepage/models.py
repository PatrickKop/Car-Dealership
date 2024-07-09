from django.contrib.auth.models import User
from django.db import models            #Django will create the SQL code for the database you are using here. So all the code here is python code and the sql is behind the scenes

# Create your models here.

class CarMake(models.Model):
    make = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.make

class CarModel(models.Model):
    model = models.CharField(max_length=100, default='')
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make.make} {self.model}"

class CarColor(models.Model):
    color = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.color

class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    color = models.ForeignKey(CarColor, on_delete=models.CASCADE)
    year = models.IntegerField(default=0)
    miles = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.year} {self.model.make.make} {self.model.model} in {self.color.color}"

class customers(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField                           

class employees(models.Model):
    #created_at = models.DateTimeField(auto_now_add=True)
    employeeFirstName = models.CharField(max_length=50, default='')
    employeeLastName = models.CharField(max_length=50, default='')
    employeeEmail = models.CharField(max_length=100, default='')                  
    employeePhone = models.CharField(max_length=15, default='')
    employeeAddress =models.CharField(max_length=100, default='')
    employeeCity = models.CharField(max_length=50, default='')
    employeeState = models.CharField(max_length=50, default='')
    employeeZip = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return (f"{self.employeeFirstName} {self.employeeLastName}")
    



#class inventory(models.Model):
    