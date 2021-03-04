# qx-user-message

my django project user message center

#### Depends:

    qx-base

### Install:

    $ pip install -e git://github.com/qx-oo/qx-base.git@1.0.2#egg=qx-base
    $ pip install -e git://github.com/qx-oo/qx-user-message.git@master#egg=qx-user-message

### Usage:

settings.py:

    INSTALLED_APPS = [
        ...
        'qx_base.qx_core',
        'qx_user_message',
        ...
    ]

    QX_USERMESSAGE_SETTINGS = {
        "MESSAGE_MODEL_CLASS": 'qx_test.user_message.models.UserMessage',
        "MESSAGE_SEND_CALLBACK": lambda empty: empty,
    }

models.py:

    from qx_user_message.models import UserMessage as QxUserMessage

    class UserMessage(QxUserMessage):

        type_map_model = {
            'user': 'auth.User',
            'test': None,
        }

        class Meta:
            verbose_name = 'UserMessage'
            verbose_name_plural = verbose_name