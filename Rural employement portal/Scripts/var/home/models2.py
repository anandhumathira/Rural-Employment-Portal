from django.db import models

class panchayath(models.Model):
    panchayath_name=models.CharField(max_length=255)
    panchayath_address=models.CharField(max_length=255)
    panchayath_district=models.CharField(max_length=255)
    panchayath_city=models.CharField(max_length=255)
    panchayath_pincode=models.CharField(max_length=255)
    panchayath_contact=models.CharField(max_length=10)
    panchayath_email=models.EmailField(max_length=255,unique=True,error_messages={'unique': 'This email address is already in use.'})
    panchayath_password=models.CharField(max_length=255)
    usertype=models.CharField(max_length=255,default='panchayath')