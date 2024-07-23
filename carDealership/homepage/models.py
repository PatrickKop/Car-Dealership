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

class customer(models.Model):
    customerFirstName = models.CharField(max_length=50, default='')
    customerLastName = models.CharField(max_length=50, default='')
    customerEmail = models.CharField(max_length=100, default='')                  
    customerPhone = models.CharField(max_length=15, default='')
    customerAddress =models.CharField(max_length=100, default='')
    customerCity = models.CharField(max_length=50, default='')
    customerState = models.CharField(max_length=50, default='')
    customerZip = models.CharField(max_length=20, default='')

    def __str__(self):
        return (f"{self.customerFirstName} {self.customerLastName}")                  

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
    



class Order(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return (f"{self.id} by {self.customer}")

class OrderItem(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return(f"{self.order.customer} bought {self.quantity} {self.car}")

class Cart(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return(f"{self.customer} bought {self.quantity} {self.car}")