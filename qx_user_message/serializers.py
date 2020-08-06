from rest_framework import serializers
from qx_base.qx_core.tools import DictInstance
from .settings import usermessage_settings


message_model = usermessage_settings.MESSAGE_MODEL_CLASS


class UserMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = message_model
        fields = ("id", "is_read", "created", "detail",)
        read_only_fields = ("id", "created", "detail",)


class BulkUpdateUserMessageSerializer(serializers.Serializer):

    type = serializers.ChoiceField(
        list(message_model.type_map_model.keys()), label="消息类型",
        required=False)

    def create(self, validated_data):
        _type = validated_data.get('type', None)
        if _type:
            message_model.objects.filter(
                type=_type,
                user_id=self.context['request'].user.id,
            ).update(is_read=True)
        else:
            message_model.objects.filter(
                user_id=self.context['request'].user.id,
            ).update(is_read=True)
        return DictInstance(data=validated_data)
