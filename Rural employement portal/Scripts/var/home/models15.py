from django.db import models

class newwork(models.Model):
    fullname=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    adharno=models.IntegerField(null=True)
    district=models.CharField(max_length=255)
    panchayath=models.CharField(max_length=255)
    contactno=models.CharField(max_length=255)
    empid=models.IntegerField(null=True)
