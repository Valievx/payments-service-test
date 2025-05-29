from django.contrib import admin

from .models import Organization, Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'operation_id', 'amount', 'document_number',
        'document_data', 'organization', 'created_at'
    )
    search_fields = ('operation_id',)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'inn', 'balance')
    search_fields = ('inn',)
    readonly_fields = ('balance',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Organization, OrganizationAdmin)
