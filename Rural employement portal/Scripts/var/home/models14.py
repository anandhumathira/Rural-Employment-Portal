from django.db import models

class empattendence(models.Model):
    attendence_choice = (('P', 'Present'),
        ('A', 'Absent'))
    employeeid = models.IntegerField(null=True)
    attendence =models.CharField(max_length=1, choices=attendence_choice)
    current_date = models.DateField(null=True)