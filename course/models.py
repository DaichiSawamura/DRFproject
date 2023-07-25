from django.db import models

from user.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса')
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
