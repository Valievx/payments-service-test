from django.urls import path

from .views import PaymentAPIView

urlpatterns = [
    path('bank/', PaymentAPIView.as_view(), name='bank'),
]
