import uuid

from django.conf import settings
from django.db import models

from lesson.models import Lesson
from user.models import NULLABLE, User


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса')
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    url_video = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    price = models.PositiveIntegerField(default=500, verbose_name='цена')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Subscription(models.Model):
    status = models.BooleanField(default=True, verbose_name='Статус подписки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class StripeCheckoutSession(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stripe_id = models.CharField(max_length=255, unique=True, editable=False)
    product = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    customer_email = models.EmailField(null=True, blank=True)
