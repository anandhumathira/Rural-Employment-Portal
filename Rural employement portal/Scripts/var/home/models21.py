from django.db import models

class admin(models.Model):
    emailid=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    usertype=models.CharField(max_length=15,default='admin')