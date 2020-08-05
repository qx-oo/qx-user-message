from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField


User = get_user_model()


class UserMessageManager(models.Manager):
    """
    UserMessage Manager
    """

    pass


class UserMessage(models.Model):

    type = models.CharField(
        verbose_name="类型", max_length=10, db_index=True)
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
    def load_related_objects(queryset, type_model_map):
        type_data = {}
        for instance in queryset:
            type_data.setdefault(instance._type, )

    class Meta:
        abstract = True
