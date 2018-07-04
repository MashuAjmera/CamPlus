from django.db import models

# Create your models here.
class buswd(models.Model):
    frm = models.CharField(max_length=256)
    to = models.CharField(max_length=256)
    time = models.TimeField()
    busno = models.IntegerField(null=True)
    operator = models.CharField(max_length=256)

class buswe(models.Model):
    frm = models.CharField(max_length=256)
    to = models.CharField(max_length=256)
    time = models.TimeField()
    busno = models.IntegerField(null=True)
    operator = models.CharField(max_length=256)
