from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.serializers import SubscriptionSerializer
from services.models import Subscription

class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
