import logging

from django.core.validators import MinValueValidator
from rest_framework import serializers

from api import consts
from payment.consts import MAX_INN_LENGTH, MIN_INN_LENGTH
from payment.models import Organization, Payment
from payment.validators import inn_validator

logger = logging.getLogger(__name__)


class PaymentReadSerializer(serializers.ModelSerializer):
    """Serializer for representation Payment info."""

    class Meta:
        model = Payment
        fields = (
            'operation_id',
            'amount',
            'payer_inn',
            'document_number',
            'document_date',
        )


class PaymentWriteSerializer(serializers.Serializer):
    """Serializer for create payment."""

    operation_id = serializers.CharField(
        max_length=consts.CHAR_MAX_LENGTH, required=True
    )
    amount = serializers.IntegerField(
        validators=[MinValueValidator(consts.MIN_VALUE)], required=True
    )
    payer_inn = serializers.CharField(
        min_length=MIN_INN_LENGTH,
        max_length=MAX_INN_LENGTH,
        validators=[
            inn_validator,
        ],
        required=True,
    )
    document_number = serializers.CharField(
        max_length=consts.CHAR_MAX_LENGTH, required=True
    )
    document_date = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        payer_inn = validated_data.pop('payer_inn')
        amount = validated_data['amount']
        organization, _ = Organization.objects.get_or_create(inn=payer_inn)
        organization.balance += amount
        logger.info(
            f'Баланс организации {organization.inn} изменен на '
            f'{amount}. {organization.balance - amount} -> '
            f'{organization.balance}'
        )
        organization.save()
        instance = Payment.objects.create(
            payer_inn=organization, **validated_data
        )
        return instance

    def to_representation(self, instance):
        return PaymentReadSerializer(instance=instance).data
