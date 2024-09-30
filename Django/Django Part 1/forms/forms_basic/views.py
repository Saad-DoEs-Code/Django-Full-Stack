from django.shortcuts import render
from . import forms
from forms_basic.forms import User
from forms_basic.forms import NewUserForm

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

def user(request):

    user_reg_form = NewUserForm()

    if request.method == "POST":
        user_reg_form = NewUserForm(request.POST)

        if user_reg_form.is_valid():
            print("Validation Success")
            user_reg_form.save(commit=True)
            print("Name:", user_reg_form.cleaned_data["name"])
            # print("Email:", user_reg_form.cleaned_data["email"])
            # print("Password:", user_reg_form.cleaned_data["password"])
            return index(request)


    return render(request, "basic/user.html", {"user_reg_form": user_reg_form})
