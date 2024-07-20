from django.contrib import admin
from .models import employees, CarColor, CarMake, CarModel, Car, customer


# Register your models here.
admin.site.register(employees)
admin.site.register(CarColor)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(customer)
