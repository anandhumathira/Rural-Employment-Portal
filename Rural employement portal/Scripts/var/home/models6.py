from django.db import models

class notifition(models.Model):
    notification=models.TextField(max_length=255)
    date=models.DateField(null=True)
    user=models.CharField(max_length=15)
   