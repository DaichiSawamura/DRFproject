from django.db import models

from user.models import NULLABLE


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)
    link = models.CharField(max_length=100, verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
