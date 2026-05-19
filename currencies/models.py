from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.code


class ExchangeRate(models.Model):
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='rates'
    )

    rate_to_usd = models.DecimalField(
        max_digits=20,
        decimal_places=4
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.currency.code} - {self.rate_to_usd}"