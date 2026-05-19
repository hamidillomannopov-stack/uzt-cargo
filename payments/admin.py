from django.contrib import admin
from .models import DriverPayment


@admin.register(DriverPayment)
class DriverPaymentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'load',
        'amount',
        'currency',
        'payment_method',
        'created_at',
    )

    search_fields = (
        'load__title',
    )