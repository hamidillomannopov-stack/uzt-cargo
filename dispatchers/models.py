from django.db import models

from finance.models import PaymentMethod
from currencies.models import Currency


class Dispatcher(models.Model):

    full_name = models.CharField(max_length=255)

    phone = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    company = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    commission_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    commission_currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name