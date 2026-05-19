from django.contrib import admin
from django.utils.html import format_html

from .models import Load
from payments.models import DriverPayment


class DriverPaymentInline(admin.TabularInline):
    model = DriverPayment
    extra = 1


@admin.register(Load)
class LoadAdmin(admin.ModelAdmin):

    class Media:
        css = {
            'all': ('loads/admin.css',)
        }

    list_display = (
        'colored_title',
        'client',
        'from_city',
        'to_city',
        'client_price',
        'client_paid_amount',
        'client_remaining_balance',
        'driver_price',
        'total_paid',
        'remaining_balance',
        'profit',
        'colored_status',
        'broker',
        'broker_fee',
    )

    list_filter = ('status',)

    search_fields = (
        'title',
        'from_city',
        'to_city',
    )

    inlines = [DriverPaymentInline]

    def colored_title(self, obj):

        colors = {
            'new': '#3498db',
            'in_progress': '#f1c40f',
            'delivered': '#2ecc71',
            'cancelled': '#e74c3c',
        }

        bg_colors = {
            'new': 'rgba(52,152,219,0.15)',
            'in_progress': 'rgba(241,196,15,0.15)',
            'delivered': 'rgba(46,204,113,0.15)',
            'cancelled': 'rgba(231,76,60,0.15)',
        }

        return format_html(
            '''
            <div style="
                background-color: {};
                padding: 8px;
                border-radius: 6px;
                font-weight: bold;
                color: {};
            ">
                {}
            </div>
            ''',
            bg_colors.get(obj.status),
            colors.get(obj.status),
            obj.title
        )

    colored_title.short_description = 'Load'

    def colored_status(self, obj):

        colors = {
            'new': '#3498db',
            'in_progress': '#f1c40f',
            'delivered': '#2ecc71',
            'cancelled': '#e74c3c',
        }

        return format_html(
            '<strong style="color:{};">{}</strong>',
            colors.get(obj.status),
            obj.get_status_display()
        )

    colored_status.short_description = 'Status'