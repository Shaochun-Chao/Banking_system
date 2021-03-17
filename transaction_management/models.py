from django.db import models
from account_management.models import Account

# Create your models here.
class MoneyTransfers(models.Model):
    transfer_id = models.AutoField(primary_key=True)
    from_account = models.ForeignKey(Account,default=None,on_delete=models.CASCADE, related_name='from_account')
    to_account = models.ForeignKey(Account,default=None,on_delete=models.CASCADE, related_name='to_account')
    amount = models.FloatField(default=0)
