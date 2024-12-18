from rest_framework import serializers
from .models import Notification

# SERIALIZER CLASS FOR NOTIFICATION

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')
    target_object = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient_username', 'actor_username', 'verb',  'target_object']

    def get_target_object(self, obj):
        # Provides a string representation of the target
        return str(obj.target)
