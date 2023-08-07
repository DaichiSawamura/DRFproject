from django.urls import path

from user.apps import UserConfig
from user.views import PaymentListAPIView

app_name = UserConfig.name

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name="payment-list"),
]
