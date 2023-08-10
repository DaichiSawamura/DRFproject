from django.urls import path

from user.apps import UserConfig
from user.views import PaymentListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UserConfig.name

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name="payment-list"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
