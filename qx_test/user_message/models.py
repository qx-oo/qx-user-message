from qx_user_message.models import UserMessage as QxUserMessage


class UserMessage(QxUserMessage):

    type_map_model = {
        'user': 'auth.User',
        'test': None,
    }

    class Meta:
        verbose_name = 'UserMessage'
        verbose_name_plural = verbose_name
