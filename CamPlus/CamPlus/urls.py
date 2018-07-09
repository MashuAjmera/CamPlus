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
from CamPlus.views import index
import datetime

# try:
#     if datetime.date-lastupdat>7:
#         lastupdat = datetime.date
#         from trans import busentry
#         busentry.busupdate()
#         print("Updated Bus")
#         from mess import menuentry
#         menuentry.menuupd()
#         print("Updated Menu")
#         from lecture import lectentry
#         lectentry.timetableupd()
#         print("Updated Time Table")
# except:
#     lastupdat = datetime.date
#     from trans import busentry
#     busentry.busupdate()
#     print("Updated Bus")
#     from mess import menuentry
#     menuentry.menuupd()
#     print("Updated Menu")
#     lectentry.timetableupd()
#     print("Updated Time Table")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('trans/',include("trans.urls")),
    path('mess/',include("mess.urls")),
    path('lecture/',include("lecture.urls")),
]
