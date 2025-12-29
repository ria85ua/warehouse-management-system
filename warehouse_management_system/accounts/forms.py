from django import forms
from django.contrib.auth.models import User
from accounts.models import Account

class RegistrationForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-md border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-500"
        }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full rounded-md border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-500"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full rounded-md border border-slate-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-slate-500"
            }),
        }


class AccountForm (forms.ModelForm):
    class Meta:
        model = Account
        fields = ('profile_pic',)

