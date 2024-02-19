from django.db import models
from accounts.models import UserAccount
# Create your models here.

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('borrow', 'Borrow'),
        ('return', 'Return'),
    )

    account = models.ForeignKey(UserAccount,related_name='transactions',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits =12,decimal_places =2)
    balance_after_transaction =models.DecimalField( max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places=2)

    time_stamp = models.DateTimeField(auto_now_add =True)
    class Meta:
        ordering = ['time_stamp']
    