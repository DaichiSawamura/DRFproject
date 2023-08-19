from django.urls import path


from user.apps import UserConfig
from user.views import PaymentListAPIView, UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UserConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name="User-create"),
    path('list/', UserListAPIView.as_view(), name="User-list"),
    path('list/<int:pk>/', UserRetrieveAPIView.as_view(), name="User-get"),
    path('list/update/<int:pk>/', UserUpdateAPIView.as_view(), name="User-update"),
    path('list/delete/<int:pk>/', UserDestroyAPIView.as_view(), name="User-delete"),
    path('payment/', PaymentListAPIView.as_view(), name="payment-list"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
