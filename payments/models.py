from django.db import models

from loads.models import Load
from currencies.models import Currency
from finance.models import PaymentMethod


class DriverPayment(models.Model):

    load = models.ForeignKey(
        Load,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )

    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE
    )
    
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    comment = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.load.title} - {self.amount}"