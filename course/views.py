from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from course.models import Course
from course.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

