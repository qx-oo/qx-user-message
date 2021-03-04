import json
from celery.task import Task
from .settings import usermessage_settings


send_callback = usermessage_settings.MESSAGE_SEND_CALLBACK
message_model = usermessage_settings.MESSAGE_MODEL_CLASS


class SendUserMessage(Task):

    def run(self, _type, object_id, from_user, to_user, detail: str):
        data = {
            "type": _type,
            "object_id": object_id,
            "from_user_id": from_user,
            "user_id": to_user,
            "detail": json.loads(detail),
        }
        instance = message_model.objects.create(**data)
        send_callback(instance)
        return instance.id
