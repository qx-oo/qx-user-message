from rest_framework import serializers
from .settings import usermessage_settings


message_model = usermessage_settings.MESSAGE_MODEL_CLASS


class UserMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = message_model
        fields = ("id", "is_read", "created", "detail")
