from django.shortcuts import render
from login.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

# Create your views here.

def signin(request):
    dicti=dict()
    if request.user.is_active:
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            dicti['error'] = True

    else:
        pass

    return render(request,'login/signin.html',context = dicti)

def signup(request):
    dicti=dict()
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            try:
                validate_password(user.password)
            except:
                dicti['error'] = "Password Entered Is Too Week To Be Accepted."
                dicti['user_form'] = UserForm()
                dicti['profile_form'] = UserProfileInfoForm()
                return render(request,'login/signup.html',context=dicti)
            if User.objects.filter(email__iexact=user.email):
                dicti['error'] = "Please Select A New E-Mail. This E-Mail is already In Use."
                dicti['user_form'] = UserForm()
                dicti['profile_form'] = UserProfileInfoForm()
                return render(request,'login/signup.html',context=dicti)
            else:
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return HttpResponseRedirect(reverse('login:signin'))
        else:
            dicti['error'] = "Please Select A New User Name. This User Name is already In Use."
            dicti['user_form'] = UserForm()
            dicti['profile_form'] = UserProfileInfoForm()
    else:
        dicti['user_form'] = UserForm()
        dicti['profile_form'] = UserProfileInfoForm()

    return render(request,'login/signup.html',context=dicti)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:signin'))
