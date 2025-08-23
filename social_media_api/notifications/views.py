from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    API view to get a list of notifications for the current user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get all notifications for the authenticated user, ordered by date
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')