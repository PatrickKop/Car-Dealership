from django.db import models            #Django will create the SQL code for the database you are using here. So all the code here is python code and the sql is behind the scenes

# Create your models here.
class cars(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

class customers(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField                           #look up more features for email

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
    