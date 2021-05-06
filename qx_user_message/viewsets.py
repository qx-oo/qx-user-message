from rest_framework import viewsets, decorators
from rest_framework.permissions import (
    IsAuthenticated,
)
from qx_base.qx_rest import mixins
from qx_base.qx_rest.response import ApiResponse
from .models import UserMessage
from .serializers import (
    UserMessageSerializer,
    BulkUpdateUserMessageSerializer,
)


class UserMessageViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.PostModelMixin,):
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
    queryset = UserMessage.objects.all().order_by('-created')
    filter_fields = ('is_read',)

    def get_serializer_class(self):
        if self.action == 'update_bulk':
            return BulkUpdateUserMessageSerializer
        return UserMessageSerializer

    def _list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        UserMessage.load_user(page)
        serializer = self.get_serializer(page, many=True)
        return self.paginator.get_paginated_data(serializer.data)

    def _retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        UserMessage.load_user(instance)
        serializer = self.get_serializer(instance)
        return serializer.data

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(user_id=self.request.user.id)
        return self.queryset

    @decorators.action(methods=['put'], url_path='bulk-read', detail=False)
    def update_bulk(self, request, *args, **kwargs):
        return ApiResponse(self._create(request, *args, **kwargs))
