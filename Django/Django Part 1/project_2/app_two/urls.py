from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("help/", views.help, name= "help"),
    path("user/", views.display_users, name= "display_users")
]