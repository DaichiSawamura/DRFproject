from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from user.models import Payment
from user.serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['payment_date']
    search_fields = ['payment_course', 'payment_lesson', 'payment_cash', 'payment_transfer']




