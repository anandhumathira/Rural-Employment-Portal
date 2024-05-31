from django.db import models

class workassign(models.Model):
    workrequestid=models.TextField(max_length=100)
    adsid=models.TextField(max_length=100)
    currentdate=models.DateField(null=True)