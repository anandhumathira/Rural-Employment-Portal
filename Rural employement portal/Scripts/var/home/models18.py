from django.db import models


class salary(models.Model):
    name_of_cardholder=models.CharField(max_length=100)
    amount=models.IntegerField(null=True)
    card_number=models.IntegerField(null=True)
    cvv=models.IntegerField(null=True)
    card_expiry=models.CharField(max_length=25)
    current_date=models.DateField(null=True)
    worker_id=models.CharField(max_length=100)