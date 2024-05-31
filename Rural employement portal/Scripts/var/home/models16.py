from django.db import models

class feedbacks(models.Model):
    feedback=models.TextField(max_length=255)
    currentdate=models.DateField(null=True)
    employeeid=models.CharField(max_length=25)