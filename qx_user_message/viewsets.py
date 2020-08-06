from rest_framework import viewsets, decorators
from rest_framework.permissions import (
    IsAuthenticated,
)
from qx_base.qx_rest import mixins
from qx_base.qx_rest.response import ApiResponse
from .serializers import (
    UserMessageSerializer,
    BulkUpdateUserMessageSerializer,
    message_model,
)


class UserMessageViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.PostModelMixin,
                         mixins.UpdateModelMixin,):
    """
    User Message
    ____
        list:
            获取消息列表

            获取消息列表

        update:
            更新消息

            更新消息

        update_bulk:
            批量更新消息

            批量更新消息
    """

    permission_classes = (
        IsAuthenticated,
    )
    queryset = message_model.objects.all().order_by('-created')
    filter_fields = ('is_read',)

    def get_serializer_class(self):
        if self.action == 'update_bulk':
            return BulkUpdateUserMessageSerializer
        return UserMessageSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(user_id=self.request.user.id)
        return self.queryset

    @decorators.action(methods=['put'], url_path='bulk-read', detail=False)
    def update_bulk(self, request, *args, **kwargs):
        return ApiResponse(self._create(request, *args, **kwargs))
