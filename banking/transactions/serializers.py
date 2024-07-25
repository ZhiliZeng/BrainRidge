# transactions/serializers.py
from rest_framework import serializers
from .models import UserAccount, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'name', 'balance']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount', 'timestamp']


