from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import Transactions
from api.serializers import TransactionSerializer, TransactionRequestSerializer, TransactionResponseSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'transactions': reverse('transactions-list', request=request, format=format),
        'transactions/record': reverse('transaction-create', request=request, format=None),
    })


class TransactionsList(generics.ListAPIView):
    """
    List all Transactions
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveAPIView):
    """
    Display a specific Transaction
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class TransactionCreate(generics.CreateAPIView):
    """
    List all Transactions, or create a new Transaction.
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionRequestSerializer


class TransactionUpdate(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a Transaction instance.
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionResponseSerializer
