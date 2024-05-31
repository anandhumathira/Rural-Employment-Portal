from django.db import models

class reply2(models.Model):
    replyid=models.CharField(max_length=255)
    reply=models.CharField(max_length=255)
    redate=models.DateField(null=True)
