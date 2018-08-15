"""CamPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from CamPlus import views

admin.site.site_header = 'CamPlus Administration'
admin.site.site_title = 'CamPlus Administration'

urlpatterns = [
    path('manshu/administrator/', admin.site.urls),
    path('index/',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('terms/',views.terms,name="terms"),
    path('cookies/',views.cookies,name="cookies"),
    path('privacy/',views.privacy,name="privacy"),
    path('feedback/',views.feedback,name="feedback"),
    path('',include("login.urls")),
    path('trans/',include("trans.urls")),
    path('mess/',include("mess.urls")),
    path('lecture/',include("lecture.urls")),
]
