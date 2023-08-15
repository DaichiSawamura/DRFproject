
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from config import settings
from course.models import Course, StripeCheckoutSession
from course.serializers import CourseSerializer
import stripe
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404, redirect


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [AllowAny]


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Course, pk=kwargs['pk'])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': product.stripe_price_data,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.DOMAIN + reverse('success') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.DOMAIN + reverse('cancel'),
        )

        StripeCheckoutSession.objects.create(
            stripe_id=checkout_session.stripe_id,
            product=product,
            status=checkout_session['status'],
        )

        return redirect(checkout_session.url)

