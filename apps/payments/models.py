from django.db import models

from apps.organizations.models import Organization


class Payment(models.Model):
    operation_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    document_number = models.CharField(max_length=100)
    document_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(
        Organization,
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
