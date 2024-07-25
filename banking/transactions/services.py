from decimal import Decimal
from django.core.exceptions import ValidationError
from .models import UserAccount, Transaction


def create_user_account(name: str, initial_balance: Decimal) -> UserAccount:
    account = UserAccount(name=name, balance=initial_balance)
    account.save()
    return account


def transfer_funds(from_account_id: int, to_account_id: int, amount: Decimal) -> Transaction:
    if amount <= 0:
        raise ValidationError("Transfer amount must be positive")

    from_account = UserAccount.objects.get(id=from_account_id)
    to_account = UserAccount.objects.get(id=to_account_id)

    if from_account.balance < amount:
        raise ValidationError("Insufficient funds")

    from_account.balance -= amount
    to_account.balance += amount

    from_account.save()
    to_account.save()

    transaction = Transaction(from_account=from_account, to_account=to_account, amount=amount)
    transaction.save()
    return transaction


def get_transaction_history(account_id: int):
    account = UserAccount.objects.get(id=account_id)
    outgoing = account.outgoing_transactions.all()
    incoming = account.incoming_transactions.all()
    return outgoing, incoming
