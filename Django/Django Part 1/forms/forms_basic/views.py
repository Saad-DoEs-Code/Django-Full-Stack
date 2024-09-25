from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):

    return render(request, "basic/index.html")

def form_data(request):

    form = forms.User()

    if request.method == "POST":
        
        form = forms.User(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name:", form.cleaned_data["name"])
            print("Email:", form.cleaned_data["email"])
            print("Password:", form.cleaned_data["password"])


    return render(request, "basic/form_page.html", {"form": form})