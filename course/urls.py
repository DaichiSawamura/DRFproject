from django.urls import path

from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet, CreateCheckoutSessionView, SubscriptionCreateAPIView, SubscriptionUpdateView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(),
                       name='create-checkout-session'),
                  path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='create'),
                  path('subscription/<int:pk>/update', SubscriptionUpdateView.as_view(), name='update')
              ] + router.urls
