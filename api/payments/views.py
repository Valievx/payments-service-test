from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PaymentSerializer
from apps.payments.models import Payment


class PaymentAPIView(APIView):
    def post(self, request):
        operation_id = request.data.get('operation_id')

        if operation_id and Payment.objects.filter(operation_id=operation_id).exists():
            payment = Payment.objects.get(operation_id=operation_id)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
