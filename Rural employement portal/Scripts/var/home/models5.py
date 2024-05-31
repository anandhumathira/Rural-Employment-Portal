from django.db import models

class workrequest(models.Model):
    address=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    panchayath=models.CharField(max_length=255)
    wardno=models.CharField(max_length=255)
    rationcardno=models.CharField(max_length=100)
    taxno=models.CharField(max_length=255)
    land_tax_receipt=models.FileField(upload_to='uploads/')
    area=models.CharField(max_length=255)
    user=models.IntegerField(null=True)
    