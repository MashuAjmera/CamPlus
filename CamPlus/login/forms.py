from django import forms
from django.contrib.auth.models import User
from login.models import UserProfileInfo

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control formback','placeholder':'First Name'}),)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control formback','placeholder':'Last Name'}),)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control formback','placeholder':'User Name'}),)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control formback','placeholder':'Email'}),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control formback','placeholder':'Password'}),)

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    # institute = forms.CharField(widget=forms.SelectInput(attrs={'class':'form-control','placeholder':'Institute'}),)
    # year = forms.CharField(widget=forms.SelectInput(attrs={'class':'form-control','placeholder':'Institute'}),)

    class Meta():
        model = UserProfileInfo
        fields = ('institute','year')
