# Generated by Django 4.2.3 on 2023-08-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_options_remove_user_username_user_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='пользователь')),
                ('payment_date', models.DateTimeField(auto_now=True, verbose_name='дата оплаты')),
                ('payment_course', models.BooleanField(default=False, verbose_name='оплачен курс')),
                ('payment_lesson', models.BooleanField(default=False, verbose_name='оплачен урок')),
                ('payment_amount', models.IntegerField(default=0, verbose_name='сумма оплаты')),
                ('payment_cash', models.BooleanField(default=False, verbose_name='оплата наличными')),
                ('payment_transfer', models.BooleanField(default=False, verbose_name='оплата переводом')),
            ],
        ),
    ]
