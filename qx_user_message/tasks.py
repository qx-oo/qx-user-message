import json
from celery.task import task
from .settings import usermessage_settings


send_callback = usermessage_settings.MESSAGE_SEND_CALLBACK
message_model = usermessage_settings.MESSAGE_MODEL_CLASS


class SendUserMessage(task):

    def run(self, _type, from_user, to_user, detail: 'dumps dict'):
        instance = message_model.objects.create({
            "type": _type,
            "from_user_id": from_user,
            "user_id": to_user,
            "detail": json.loads(detail)
        })
        send_callback(instance)
