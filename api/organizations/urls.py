from django.urls import path

from .views import OrganizationBalanceAPIView

urlpatterns = [
    path('<str:inn>/balance/', OrganizationBalanceAPIView.as_view(), name='organization-balance')
]
