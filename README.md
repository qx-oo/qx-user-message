# qx-platform-auth

my django project thirdparty platform auth

#### Depends:

    qx-base

### Install:

    pip install -e -e git://github.com/qx-oo/qx-base.git@1.0.2#egg=qx-base
    pip install -e git://github.com/qx-oo/qx-user-message.git@master#egg=qx-user-message

### Usage:

settings.py:

    INSTALLED_APPS = [
        ...
        'qx_base.qx_core',
        ''
        ...
    ]