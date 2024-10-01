from django.urls import path
from . import views

app_name = "app_1"

urlpatterns = [
    path("other/", views.others, name="other"),
    path("relative/", views.relative, name="relative"),
]