from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    college = (
        ('LNMIIT','The LNM Institute Of Information Technology'),
        ('VIT','Vellore Institute Of Technology'),
        ('SRM','Sri Ramaswamy Memorial Institute'),
    )
    yearch = (
        ('Y18','Batch Of 2018'),
        ('Y17','Batch Of 2017'),
        ('Y16','Batch Of 2016'),
        ('Y15','Batch Of 2015'),
    )
    # Add any additional attributes you want
    institute = models.CharField(max_length=10, choices=college)
    year = models.CharField(max_length = 3,choices = yearch)

    def __str__(self):
        return self.user.username
