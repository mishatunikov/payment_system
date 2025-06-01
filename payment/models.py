from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from payment import consts
from payment.validators import inn_validator


class Organization(models.Model):
    """Organization Model."""

    inn = models.CharField(
        verbose_name='ИНН',
        validators=[
            inn_validator,
        ],
        max_length=consts.MAX_INN_LENGTH,
        unique=True,
        db_index=True,
    )
    balance = models.BigIntegerField(
        verbose_name='баланс',
        default=consts.DEFAULT_BALANCE,
    )

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'Организации'
        ordering = ('inn',)

    def __str__(self):
        return f'Организация {self.inn}'


class Payment(models.Model):
    """Payment Model."""

    operation_id = models.CharField(
        max_length=consts.CHAR_MAX_LENGTH,
        verbose_name='идентификатор',
        unique=True,
        db_index=True,
    )
    amount = models.BigIntegerField(
        verbose_name='Сумма транзакции',
    )
    payer_inn = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='payments',
        to_field='inn',
    )
    document_number = models.CharField(max_length=consts.CHAR_MAX_LENGTH)
    document_date = models.DateTimeField(
        verbose_name='дата создания документа'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='дата добавления в бд'
    )

    class Meta:
        verbose_name = 'транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ('-document_date',)

    def __str__(self):
        return f'Транзакция {self.operation_id}: {self.amount}'
