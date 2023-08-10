from django.conf import settings
from django.db import models

from lesson.models import Lesson
from user.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса')
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
