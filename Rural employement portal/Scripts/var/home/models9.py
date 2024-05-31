from django.db import models

class workcomplete(models.Model):
    workentryid=models.CharField(max_length=255)
    completeworkdetails=models.CharField(max_length=255)
    currentdetails=models.CharField(max_length=255)
    todate=models.DateField(null=True)