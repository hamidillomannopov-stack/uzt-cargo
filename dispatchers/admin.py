from django.contrib import admin
from .models import Dispatcher


@admin.register(Dispatcher)
class DispatcherAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'full_name',
        'phone',
        'company',
        'commission_amount',
        'commission_currency',
        'payment_method',
        'is_active',
    )

    search_fields = (
        'full_name',
        'phone',
        'company',
    )

    list_filter = (
        'is_active',
    )