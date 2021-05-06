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
        "message_send_callback": lambda empty: empty,
        "message_object_map": {
            "comment": "comment.Comment",
            "star": "comment.Star",
        },
        "message_user_serializer": "user.models.SimpleUserSerializer",
    }

urls.py:

    urlpatterns_api = [
        path('', include('qx_user_message.urls')),
    ]

celery.py:

    app.conf.task_routes = {
        'qx_user_message.tasks.SendUserMessage': {
            'queue': 'default',
        },
    }