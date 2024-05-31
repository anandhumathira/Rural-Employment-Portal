from django.db import models
from.models3 import ads
from.models4 import workemployee

class reply12(models.Model):
    reply=models.TextField(max_length=255)
    sender_id=models.ForeignKey(ads,on_delete=models.CASCADE,null=True)
    reciever_id=models.ForeignKey(workemployee,on_delete=models.CASCADE,null=True)
    current_date=models.DateField(null=True)