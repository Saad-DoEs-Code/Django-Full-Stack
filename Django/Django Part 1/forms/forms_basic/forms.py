from django import forms
from django.core import validators
class User(forms.Form):

    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email",)
    verify_email = forms.EmailField(label="Confirm Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,)


    # Self Defined Cleaner for Bot Catcher 
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data["botcatcher"]

        if len(botcatcher) > 0:
            raise forms.ValidationError("Gotcha Bot!")

        return botcatcher
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        n= 4
        length = len(email)
        if email[length-n:].lower()!=".com":
            raise forms.ValidationError("Emails Should end with '.com'")
    
    # Self Defined Cleaner for Whole Form 
    def clean(self):
        # super() will grab all the cleaned data
        all_clean_data = super().clean()
        # print(all_clean_data)
        email = all_clean_data["email"]
        # print(email[:5:-1])
        v_mail = all_clean_data["verify_email"]
        name = all_clean_data["name"]
        if email != v_mail:
            raise forms.ValidationError("Emails don't match!")


        if name[0].lower() == "s":
            raise forms.ValidationError("Name can't start with S!")
        
        return all_clean_data