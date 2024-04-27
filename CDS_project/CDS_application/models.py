from django.db import models

# Create your models here.
class CDR(models.Model):
    MSISDN=models.CharField(max_length=30)
    IMSI=models.BigIntegerField()
    IMEI=models.BigIntegerField()
    PLAN=models.CharField(max_length=30)
    CALL_TYPE=models.CharField(max_length=30)
    CORRESP_TYPE=models.CharField(max_length=30)
    CORRESP_ISDN=models.CharField(max_length=30)
    DURATION=models.PositiveIntegerField()
    TIME=models.DateTimeField()
    DATE=models.CharField(max_length=30)
