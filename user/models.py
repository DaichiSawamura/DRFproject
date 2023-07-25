from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.IntegerField(unique=True, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    image = models.ImageField(**NULLABLE, verbose_name='Изображение')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
