from django.contrib import admin

from .models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'inn', 'balance')
    search_fields = ('inn',)
    readonly_fields = ('balance',)


admin.site.register(Organization, OrganizationAdmin)
