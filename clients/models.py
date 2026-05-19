from django.db import models


class Client(models.Model):

    company_name = models.CharField(max_length=255)

    manager_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    telegram_username = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name