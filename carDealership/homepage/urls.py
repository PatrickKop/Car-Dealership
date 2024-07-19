#Added Everythin below and url.py file
from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("firstpage.html", views.home, name="home"),
path("secondpage.html", views.second, name="second"),
path("inventory.html", views.inventory, name="inventory"),
path("logout/", views.logout_user, name="logout"),
path("register/", views.register_user, name="register"),
path("employees/", views.employees_list, name="employees"),
path("employeeRecord/<int:pk>", views.employees_record, name="employeeRecord"),
path("deleteEmployeeRecord/<int:pk>", views.delete_employees_record, name="deleteEmployeeRecord"),
path("addEmployee/", views.add_employee, name="addEmployee"),
path("updateEmployeeRecord/<int:pk>", views.update_employees_record, name="updateEmployeeRecord"),
path("updateCarRecord/<int:pk>", views.update_car_record, name="updateCarRecord"),
path("carRecord/<int:pk>", views.car_record, name="carRecord"),
path("addCar/", views.add_car, name="addCar"),
path('addCarMake/', views.add_car_make, name='add_car_make'),
path('addCarModel/', views.add_car_model, name='add_car_model'),
path('addCarColor/', views.add_car_color, name='add_car_color'),
path("deleteCarRecord/<int:pk>", views.delete_car_record, name="deleteCarRecord"),
path("customers/", views.customer_list, name="customers"),
path("addCustomers/", views.add_customer, name="addCustomer"),

]
