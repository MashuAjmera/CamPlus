from django.db import models

# Create your models here.
class menu(models.Model):
    day = models.CharField(max_length=256)
    brk = models.CharField(max_length=256)
    lun = models.CharField(max_length=256)
    snk = models.CharField(max_length=256)
    din = models.CharField(max_length=256)
