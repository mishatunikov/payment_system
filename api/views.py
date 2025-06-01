from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PaymentReadSerializer, PaymentWriteSerializer
from payment.models import Payment


class PaymentAPIView(APIView):

    def post(self, request):
        serializer = PaymentWriteSerializer(
            data=request.data, context=request.data
        )
        serializer.is_valid(raise_exception=True)
        operation_id = request.data['operation_id']

        if payment := Payment.objects.filter(operation_id=operation_id).first():
            return Response(
                PaymentReadSerializer(payment).data, status=status.HTTP_200_OK
            )

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
