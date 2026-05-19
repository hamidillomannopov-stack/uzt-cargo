from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'company_name',
        'manager_name',
        'phone',
    )

    search_fields = (
        'company_name',
        'manager_name',
        'phone',
    )