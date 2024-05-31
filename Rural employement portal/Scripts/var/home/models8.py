from django.db import models

class  entry12(models.Model):
    workdetails=models.CharField(max_length=255)
    startingdate=models.DateField(null=True)
    no_of_days=models.CharField(max_length=255)
    panchayathid=models.CharField(max_length=255)