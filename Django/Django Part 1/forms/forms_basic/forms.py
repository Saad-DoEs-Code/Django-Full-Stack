from django import forms

class User(forms.Form):

    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
