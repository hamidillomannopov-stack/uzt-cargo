from django.db import models

from drivers.models import Driver
from currencies.models import Currency
from clients.models import Client
from finance.models import PaymentMethod
from brokers.models import Broker
from dispatchers.models import Dispatcher


class Load(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)

    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    from_city = models.CharField(max_length=255)

    to_city = models.CharField(max_length=255)

    client_price = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )

    client_paid_amount = models.DecimalField(
    max_digits=20,
    decimal_places=2,
    default=0
)

    client_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='client_loads'
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    driver_price = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )

    driver_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='driver_loads'
    )

    broker = models.ForeignKey(
        Broker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    broker_fee = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    broker_currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='broker_currency_loads'
    )

    broker_payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='broker_payment_methods'
    )

    dispatcher = models.ForeignKey(
        Dispatcher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    dispatcher_fee = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    dispatcher_currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='dispatcher_currency_loads'
    )

    dispatcher_payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='dispatcher_payment_methods'
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_paid(self):
        return sum(
            payment.amount
            for payment in self.payments.all()
        )

    @property
    def remaining_balance(self):
        return self.driver_price - self.total_paid

        @property
    def client_remaining_balance(self):
        return self.client_price - self.client_paid_amount

        @property
    def profit(self):
        return (
            self.client_paid_amount
            - self.driver_price
            - self.broker_fee
            - self.dispatcher_fee
        )

    def __str__(self):
        return self.title