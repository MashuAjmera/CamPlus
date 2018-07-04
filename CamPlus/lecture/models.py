from django.db import models

# Create your models here.
class timetable(models.Model):
    day = models.CharField(max_length=256)
    LT = models.CharField(max_length=256)
    sltst = models.TimeField()
    slten = models.TimeField()
    year = models.CharField(max_length=256)
    teacher = models.CharField(max_length=256)
    subject = models.CharField(max_length=256)
