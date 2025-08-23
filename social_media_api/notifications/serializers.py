from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField() # Show the username of the actor
    target_object = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['actor', 'verb', 'target_object', 'timestamp', 'is_read']

    def get_target_object(self, obj):
        return str(obj.target)