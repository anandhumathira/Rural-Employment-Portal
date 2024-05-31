from django.db import models

class complaints(models.Model):
    subject=models.CharField(max_length=255)
    complaint=models.CharField(max_length=255)
    todate=models.DateField(null=True)
    user=models.IntegerField(null=True)