from django.db import models


class Driver(models.Model):
    full_name = models.CharField(max_length=255)

    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    passport_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    truck_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    telegram_id = models.BigIntegerField(
        blank=True,
        null=True
    )

    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]

    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='pending'
)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name