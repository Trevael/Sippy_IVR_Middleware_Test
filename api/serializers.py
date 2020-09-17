from rest_framework import serializers

from api.models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"
        #id = serializers.IntegerField(read_only=True)
        #cc_num = serializers.CharField(required=True, allow_blank=False, max_length=4)
        #created = serializers.IntegerField(read_only=True)
        #exp_date = serializers.CharField(required=True, allow_blank=False, max_length=4)
        #response = serializers.CharField('base_template': 'JSON')
        #response_code  = serializers.CharField(required=True, allow_blank=False, max_length=3)
        #trans_id
