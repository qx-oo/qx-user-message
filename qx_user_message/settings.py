from django.conf import settings
from django.utils.module_loading import import_string
from qx_base.qx_core.tools import DictInstance


IMPORT_LIST = [
    'MESSAGE_MODEL_CLASS',
    'MESSAGE_SEND_CALLBACK',
]


QX_USERMESSAGE_SETTINGS = {
    "MESSAGE_MODEL_CLASS": None,
    "MESSAGE_SEND_CALLBACK": None,
}

_b_settings = QX_USERMESSAGE_SETTINGS

_settings = getattr(settings, 'QX_USERMESSAGE_SETTINGS',
                    QX_USERMESSAGE_SETTINGS)

if _settings:
    _b_settings.update(_settings)


def get_attr(key, val):
    if key in IMPORT_LIST:
        if val:
            return import_string(val)
        else:
            raise ImportError('Settings {} import error.'.format(key))
    return val


usermessage_settings = DictInstance(**QX_USERMESSAGE_SETTINGS)
for key, val in _b_settings.items():
    setattr(usermessage_settings, key, get_attr(val))
