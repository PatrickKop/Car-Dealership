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

]
