from django.db import models
from django.core.validators import MinLengthValidator


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
