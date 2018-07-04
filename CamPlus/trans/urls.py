from django.contrib import admin
from django.urls import path,include
from trans import views

app_name = 'trans'

urlpatterns = [
    path('bus',views.bus,name="bus"),
    path('bus/LNMIIT',views.buslnm,name="buslnm"),
    path('bus/City',views.buscit,name="buscit"),
    path('bus/Other',views.busoth,name="busoth"),
]
