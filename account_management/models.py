from django.db import models
from user_management.models import ExternalUser

account_type = [("savings","savings"),("checking","checking"),("credit","credit")]


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_number = models.CharField(max_length=5,default=None)
    account_type = models.CharField(max_length=10,choices=account_type)
    account_balance = models.FloatField(default=0.0)
    user_id = models.ForeignKey(ExternalUser,default=None,on_delete=models.CASCADE,related_name='useridAccount')

