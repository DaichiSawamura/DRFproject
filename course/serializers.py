from rest_framework import serializers

from course.models import Course, Subscription

from lesson.serializers import LessonSerializer
from lesson.validators import UrlValidator


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, instance):
        return instance.lesson_set.all().count()

    class Meta:
        model = Course
        fields = ['title', 'image', 'description', 'lesson_count', 'lesson']
        validators = [UrlValidator(field='url_video')]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
