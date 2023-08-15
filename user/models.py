from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.IntegerField(unique=True, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    image = models.ImageField(**NULLABLE, verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='активность')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    username = models.CharField(max_length=50, verbose_name='пользователь')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='дата оплаты')
    payment_course = models.BooleanField(default=False, verbose_name='оплачен курс')
    payment_lesson = models.BooleanField(default=False, verbose_name='оплачен урок')
    payment_amount = models.IntegerField(default=0, verbose_name='сумма оплаты')
    payment_cash = models.BooleanField(default=False, verbose_name='оплата наличными')
    payment_transfer = models.BooleanField(default=False, verbose_name='оплата переводом')
