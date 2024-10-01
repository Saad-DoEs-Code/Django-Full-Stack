from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, "app_1/index.html")

def others(request):

    return render(request, "app_1/others.html")

def relative(request):

    return render(request, "app_1/rel_url_temp.html")