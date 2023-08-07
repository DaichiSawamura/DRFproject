from django.urls import path
from rest_framework.routers import DefaultRouter

from lesson.apps import LessonConfig
from lesson.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = LessonConfig.name

urlpatterns = [
    path('create/', LessonCreateAPIView.as_view(), name="lesson-create"),
    path('list/', LessonListAPIView.as_view(), name="lesson-list"),
    path('list/<int:pk>/', LessonRetrieveAPIView.as_view(), name="lesson-get"),
    path('list/update/<int:pk>/', LessonUpdateAPIView.as_view(), name="lesson-update"),
    path('list/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name="lesson-delete"),
]
