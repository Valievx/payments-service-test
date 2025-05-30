import logging

from rest_framework import serializers

from apps.payments.models import Payment
from apps.organizations.models import Organization


logger = logging.getLogger(__name__)


class PaymentSerializer(serializers.ModelSerializer):
    payer_inn = serializers.CharField(source='organization.inn', write_only=True)

    class Meta:
        model = Payment
        fields = (
            'operation_id', 'amount', 'payer_inn',
            'document_number', 'document_date',
        )

    def validate(self, data):
        if data['amount'] <= 0:
            raise serializers.ValidationError({'amount': 'Must be positive'})

        return data

    def create(self, validated_data):
        inn_data = validated_data.pop('organization')
        operation_id = validated_data['operation_id']
        amount = validated_data['amount']

        org, created = Organization.objects.get_or_create(inn=inn_data['inn'])
        new_balance = org.balance + amount
        org.balance = new_balance
        org.save()

        logger.info(
            f'Payment processed | '
            f'INN: {org.inn} | '
            f'Amount: {amount} | '
            f'Balance: {new_balance} | '
            f'Operation: {operation_id}'
        )

        payment = Payment.objects.create(organization=org, **validated_data)
        return payment
