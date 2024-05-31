from django.db import models

class ads(models.Model):
    adsname=models.CharField(max_length=255)
    adsgender = models.CharField(max_length=10)
    adsadharno=models.CharField(max_length=15)
    adsdistrict=models.CharField(max_length=255)
    adspanchayath=models.CharField(max_length=255)
    adsward=models.CharField(max_length=255)
    adscontact=models.CharField(max_length=10)
    adsemail=models.EmailField(max_length=255,unique=True,error_messages={'unique': 'This email address is already in use.'})
    adspassword=models.CharField(max_length=255)
    usertype=models.CharField(max_length=255,default='ads')
