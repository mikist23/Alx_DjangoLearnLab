from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Notification
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import NotificationSerializer

# Create your views here.

class ListNotificationView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Fetch notifications for the logged in user
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
    