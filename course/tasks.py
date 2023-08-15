from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from course.models import Subscription
from user.models import User


@shared_task
def send_mail_user_update(object_pk):
    subs_list = Subscription.objects.filter(course=object_pk)
    for item in subs_list:
        send_mail(
            subject='Обновление',
            message=f'Обновление курса(ов) {subs_list}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[item.user.email]
        )


@shared_task
def check_user():
    now_date = datetime.now()
    one_month_ago = now_date - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago)
    inactive_users.update(is_active=False)
