from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny

from user.models import Payment, User
from user.serializers import PaymentSerializer, UserSerializers


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers
    permission_classes = [AllowAny]


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['payment_date']
    search_fields = ['payment_course', 'payment_lesson', 'payment_cash', 'payment_transfer']
