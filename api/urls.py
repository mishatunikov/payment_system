from django.contrib import admin
from django.urls import include, path

from api.views import OrganizationBalanceView, PaymentAPIView

urlpatterns = [
    path('webhook/bank/', PaymentAPIView.as_view()),
    path('organizations/<inn>/balance/', OrganizationBalanceView.as_view()),
]
