from django.db import models

class pub(models.Model):
    name=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    panchayath=models.CharField(max_length=255)
    contact=models.CharField(max_length=10)
    emailid=models.EmailField(max_length=255,unique=True,error_messages={'unique': 'This email address is already in use.'})
    password=models.CharField(max_length=255)
    usertype=models.CharField(max_length=255,default='public')
