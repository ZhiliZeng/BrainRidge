from django.urls import path
from .views import create_account, transfer, transaction_history

urlpatterns = [
    path('accounts/create/', create_account, name='create_account'),
    path('accounts/transfer/', transfer, name='transfer'),
    path('accounts/<int:account_id>/transactions/', transaction_history, name='transaction_history'),
]
