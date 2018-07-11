from django.contrib import admin
from django.urls import path,include
from login.views import signin,signup,user_logout

app_name = 'login'

urlpatterns = [
    path('',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('logout/',user_logout,name="logout")
]
