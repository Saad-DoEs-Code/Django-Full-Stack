from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {"name":"Saad", "number":0}

    return render(request, "app_1/index.html", context=context_dict)

def others(request):

    return render(request, "app_1/others.html")

def relative(request):

    return render(request, "app_1/rel_url_temp.html")