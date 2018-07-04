from django.contrib import admin
from django.urls import path,include
from mess.views import menudisp

app_name = 'mess'

urlpatterns = [
    path('menu',menudisp,name="menu")
]
