from django.db import models

# Create your models here.

class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    from_account = models.ForeignKey(UserAccount, related_name='outgoing_transactions', on_delete=models.CASCADE)
    to_account = models.ForeignKey(UserAccount, related_name='incoming_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

