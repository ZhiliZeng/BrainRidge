from django.shortcuts import render

# Create your views here.
from decimal import Decimal
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from rest_framework.utils import json
from django.core.exceptions import ValidationError
import json

from .models import UserAccount
from .services import create_user_account, transfer_funds, get_transaction_history


@require_http_methods(["POST"])
def create_account(request):
    try:
        data = json.loads(request.body)
        name = data['name']
        initial_balance = Decimal(data['initial_balance'])
        account = create_user_account(name, initial_balance)
        return JsonResponse({'id': account.id, 'name': account.name, 'balance': str(account.balance)})
    except (KeyError, ValueError, ValidationError) as e:
        return HttpResponseBadRequest(str(e))


@require_http_methods(["POST"])
def transfer(request):
    try:
        data = json.loads(request.body)
        from_account_id = data['from_account_id']
        to_account_id = data['to_account_id']
        amount = Decimal(data['amount'])
        transaction = transfer_funds(from_account_id, to_account_id, amount)
        return JsonResponse({'id': transaction.id, 'from_account': transaction.from_account.id, 'to_account': transaction.to_account.id, 'amount': str(transaction.amount), 'timestamp': transaction.timestamp})
    except (KeyError, ValueError, UserAccount.DoesNotExist, ValidationError) as e:
        return HttpResponseBadRequest(str(e))


@require_http_methods(["GET"])
def transaction_history(request, account_id):
    try:
        outgoing, incoming = get_transaction_history(account_id)
        outgoing_data = [{'id': t.id, 'to_account': t.to_account.id, 'amount': str(t.amount), 'timestamp': t.timestamp} for t in outgoing]
        incoming_data = [{'id': t.id, 'from_account': t.from_account.id, 'amount': str(t.amount), 'timestamp': t.timestamp} for t in incoming]
        return JsonResponse({'outgoing': outgoing_data, 'incoming': incoming_data})
    except UserAccount.DoesNotExist as e:
        return HttpResponseBadRequest(str(e))
