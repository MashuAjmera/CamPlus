from django.contrib import admin
from django.urls import path,include
from lecture.views import ttdisp

app_name = 'lecture'

urlpatterns = [
    path('timetable',ttdisp,name="ttdisplay")
]
