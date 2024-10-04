from django.shortcuts import render
from auth_app.forms import UserForm, UserProfileInfoForm

# Create your views here.


def index(request):

    context = {}
    return render(request, "auth_app/index.html", context=context)


def register(request):

    is_registered = False
    if is_registered == False and request.method == "POST":
        user = UserForm(request.POST)
        user_profile = UserProfileInfoForm(request.POST)
        if user.is_valid() and user_profile.is_valid():
            user = user.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile.save(commit=False)
            user_profile.user = user
            if "profile_picture" in request.FILES:
                user_profile.profile_picture = request.FILES['profile_picture']
            user_profile.save()
            is_registered = True
        else:
            print(user.errors, user_profile.errors)

    else:
        user = UserForm()
        user_profile = UserProfileInfoForm()

    context_dict = {"user_form": user,
                    "user_profile_form": user_profile, "is_registered": is_registered}
    return render(request, "auth_app/register.html", context=context_dict)
