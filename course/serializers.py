from rest_framework import serializers

from course.models import Course, Subscription
from lesson.models import Lesson

from lesson.serializers import LessonSerializer
from lesson.validators import UrlValidator


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, course):
        lesson = Lesson.objects.filter(course=course)
        if lesson:
            return lesson.count()
        return 0

    class Meta:
        model = Course
        fields = ['title', 'image', 'description', 'lesson_count', 'lesson', 'price']
        validators = [UrlValidator(field='url_video')]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
