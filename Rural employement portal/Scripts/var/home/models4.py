from django.db import models
 
class workemployee(models.Model):
    emname=models.CharField(max_length=255)
    emaddress=models.CharField(max_length=255)
    empincode=models.CharField(max_length=255)
    emdistrict=models.CharField(max_length=150)
    empanchayath=models.CharField(max_length=255)
    emward=models.CharField(max_length=255)
    emratiocard=models.CharField(max_length=255)
    emadhar=models.CharField(max_length=255)
    emcontact=models.CharField(max_length=15)
    emusername=models.CharField(max_length=150,unique=True,error_messages={'unique': 'This email address is already in use.'})
    empassword=models.CharField(max_length=150)
    payment_status=models.IntegerField(null=True,default=0)
    usertype=models.CharField(max_length=255,default='employee')