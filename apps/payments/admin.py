from django.contrib import admin

from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'operation_id', 'amount', 'document_number',
        'document_date', 'organization', 'created_at'
    )
    search_fields = ('operation_id',)


admin.site.register(Payment, PaymentAdmin)
