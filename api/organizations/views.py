from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrganizationSerializer
from apps.payments.models import Organization


class OrganizationBalanceAPIView(APIView):
    def get(self, request, inn):

        try:
            org = Organization.objects.get(inn=inn)
            serializer = OrganizationSerializer(org)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Organization.DoesNotExist:
            return Response(
                {'error': 'Organization not found'},
                status=status.HTTP_404_NOT_FOUND
            )
