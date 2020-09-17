from rest_framework.generics import GenericAPIView

from api.models import Transactions
from api.serializers import TransactionSerializer


class TransactionsAPIView(GenericAPIView):
    queryset = Transactions.objects.all()
    #serializer_class = TransactionsSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(queryset=self.queryset)
        serializer = TransactionSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)
