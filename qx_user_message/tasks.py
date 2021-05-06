import json
from celery.task import Task
from .settings import usermessage_settings
from .models import UserMessage


send_callback = usermessage_settings.message_send_callback


class SendUserMessage(Task):

    def run(self, _type, object_id, from_user, to_user, detail: str):
        data = {
            "type": _type,
            "object_id": object_id,
            "from_user_id": from_user,
            "user_id": to_user,
            "detail": json.loads(detail),
        }
        instance = UserMessage.objects.create(**data)
        send_callback(instance)
        return instance.id
