from django.db import models
from django.core.validators import MinLengthValidator


class Payment(models.Model):
    operation_id = models.CharField(max_length=100)
    amount = models.IntegerField(validators=[MinLengthValidator(1)])
    document_number = models.CharField(max_length=100)
    document_data = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='payments',
        to_field='inn',
        db_column='payer_inn'
    )

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        db_table = 'payment'

    def __str__(self):
        return self.operation_id


class Organization(models.Model):
    inn = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(10)]
    )
    balance = models.IntegerField(
        default=0,
        validators=[MinLengthValidator(0)]
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        db_table = 'organization'

    def __str__(self):
        return self.inn
