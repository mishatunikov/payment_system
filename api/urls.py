from django.contrib import admin
from django.urls import include, path

from api.views import PaymentAPIView

urlpatterns = [
    path('webhook/bank/', PaymentAPIView.as_view()),
]
