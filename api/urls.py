from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('webhook/', include('api.payments.urls'), name='webhook'),
    path('organizations/', include('api.organizations.urls'), name='organizations'),
]
