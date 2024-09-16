from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {"insert_me": "Hi! I am from VIEWS.PY!!!"}
    # Context means the data being transferred
    return render(request,"first_app/index.html", context=my_dict)
