from django.db import models

# Create your models here.
class cars(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

class customers(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField                           #look up more features for email

class employees(models.Model):
    employeeID = models.IntegerField                    #need to add way to incremnet and assign automatically
    employeeFirstName = models.CharField(max_length=50)
    employeeLastName = models.CharField(max_length=50)
    employeeEmail = models.EmailField                   #look up more features for email

class inventory(models.Model):
    