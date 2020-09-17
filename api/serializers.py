from rest_framework import serializers

from api.models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class TransactionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            'cc_num',
            'cvv',
            'exp_date',
            'trans_id',
        ]

    def create(self, validated_data):
        """
        Create and return a new `Transactions` instance, given the validated data.
        """
        return Transactions.objects.create(**validated_data)


class TransactionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            'response',
            'response_code',
        ]

    def update(self, instance, validated_data):
        """
        Update and return an existing `Transactions` instance, given the validated data.
        """
        instance.response = validated_data.get('response', instance.response)
        instance.response_code = validated_data.get('response_code', instance.response_code)
        instance.save()
        return instance
