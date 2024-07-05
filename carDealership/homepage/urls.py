#Added Everythin below and url.py file
from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("firstpage.html", views.home, name="home"),
path("secondpage.html", views.second, name="second"),
path("inventory.html", views.inventory, name="inventory"),
#path("login/", views.login_user, name="login"),
path("logout/", views.logout_user, name="logout"),
path("register/", views.register_user, name="register"),
path("employees/", views.employees_list, name="employees"),
path("employeeRecord/<int:pk>", views.employees_record, name="employeeRecord"),
path("deleteEmployeeRecord/<int:pk>", views.delete_employees_record, name="deleteEmployeeRecord"),
path("addEmployee/", views.add_employee, name="addEmployee"),
path("updateEmployeeRecord/<int:pk>", views.update_employees_record, name="updateEmployeeRecord"),

]
