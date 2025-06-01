from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import (
    PaymentReadSerializer,
    PaymentWriteSerializer,
)
from payment.models import Organization, Payment


class PaymentAPIView(APIView):
    """Process a request to create a payment."""

    def post(self, request):
        serializer = PaymentWriteSerializer(
            data=request.data, context=request.data
        )
        serializer.is_valid(raise_exception=True)
        operation_id = request.data['operation_id']

        if payment := Payment.objects.filter(
            operation_id=operation_id
        ).first():
            return Response(
                PaymentReadSerializer(payment).data, status=status.HTTP_200_OK
            )

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrganizationBalanceView(APIView):
    """Returns balance of organization by INN."""

    def get(self, request, inn):
        organization = get_object_or_404(Organization, inn=inn)

        return Response(
            {'inn': organization.inn, 'balance': organization.balance}
        )
