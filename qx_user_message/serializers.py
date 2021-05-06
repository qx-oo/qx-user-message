from rest_framework import serializers
from qx_base.qx_core.tools import DictInstance
from .settings import usermessage_settings
from .models import UserMessage


UserSerializer = usermessage_settings.message_user_serializer


if UserSerializer:
    def userinfo_func(user): return UserSerializer(user).data
else:
    if usermessage_settings.has_userinfo:
        def userinfo_func(user): return user.get_simple_userinfo()
    else:
        def userinfo_func(user): return user.id


um_read_only_fields = (
    "id", "created", "detail", "user", "from_user", "type", "object_id",)


class UserMessageSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    from_user = serializers.SerializerMethodField()

    def get_user(self, instance):
        return userinfo_func(instance.user)

    def get_from_user(self, instance):
        return userinfo_func(instance.from_user)

    class Meta:
        model = UserMessage
        fields = um_read_only_fields + ('is_read', )
        read_only_fields = um_read_only_fields


class BulkUpdateUserMessageSerializer(serializers.Serializer):

    type = serializers.ChoiceField(
        list(UserMessage.type_map_model.keys()), label="消息类型",
        required=False)

    def create(self, validated_data):
        _type = validated_data.get('type', None)
        if _type:
            UserMessage.objects.filter(
                type=_type,
                user_id=self.context['request'].user.id,
            ).update(is_read=True)
        else:
            UserMessage.objects.filter(
                user_id=self.context['request'].user.id,
            ).update(is_read=True)
        return DictInstance(data=validated_data)
