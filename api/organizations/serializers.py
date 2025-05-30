from rest_framework import serializers

from apps.payments.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('inn', 'balance',)
