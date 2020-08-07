from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField
from qx_base.qx_core.models import ContentTypeRelated, load_set_queryset_object


User = get_user_model()


class UserMessage(ContentTypeRelated):

    user_id = models.IntegerField(
        verbose_name="用户Id", null=True, blank=True, db_index=True)
    from_user_id = models.IntegerField(
        verbose_name="发送用户Id", null=True, blank=True)
    is_active = models.BooleanField(
        verbose_name="是否可用", default=True)
    is_read = models.BooleanField(
        verbose_name="是否读取", default=False)
    created = models.DateTimeField(
        verbose_name='创建时间', default=timezone.now, editable=False)
    detail = JSONField(
        verbose_name="详情", default=dict)

    @staticmethod
    def load_user(queryset):
        field_map = {
            'user_id': 'user',
            'from_user_id': 'from_user'
        }
        return load_set_queryset_object(
            queryset, User, field_map, ['userinfo'])

    class Meta:
        abstract = True
