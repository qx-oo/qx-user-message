import pytest
import json
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from qx_test.user_message.models import UserMessage
from qx_user_message.tasks import SendUserMessage
from qx_user_message.viewsets import UserMessageViewSet
from rest_framework.test import force_authenticate


User = get_user_model()


class TestUserMessage:

    @pytest.mark.django_db
    def test_model(self, rf):

        user1 = User.objects.create(username="test1")
        user2 = User.objects.create(username="test2")
        user3 = User.objects.create(username="test3")
        SendUserMessage().run('user', user1.id, user1.id,
                              user2.id, detail=json.dumps({"title": "hello"}))
        SendUserMessage().run('test', None, user3.id,
                              user2.id, detail=json.dumps({"title": "hello"}))
        message_list = list(UserMessage.objects.filter(user_id=user2.id))
        assert len(message_list) > 1

        request = rf.get('/api/tests/user-message/')
        # request.user = user2
        force_authenticate(request, user2)
        views = csrf_exempt(UserMessageViewSet.as_view({'get': 'list'}))
        response = views(request)
        data = json.loads(response.content)
        assert len(data['data']['results']) > 1

        req_data = {
            'type': 'user',
        }
        request = rf.put('/api/tests/user-message/bulk-read/', data=req_data)
        force_authenticate(request, user2)
        views = csrf_exempt(UserMessageViewSet.as_view({'put': 'update_bulk'}))
        breakpoint()
        response = views(request)
        assert response.status_code == 200

        # user1 = User.objects.get(account='18866668881')
        # user2 = User.objects.get(account='18866668882')
        # user3 = User.objects.get(account='18866668883')
        # Baby.objects.create(name='test1', type="user",
        #                     object_id=user1.id, user_id=user1.id,)
        # Baby.objects.create(name='test2', type="user",
        #                     object_id=user2.id, user_id=user2.id,)
        # Baby.objects.create(name='test3', type="user",
        #                     object_id=user3.id, user_id=0,)
        # Baby.objects.create(name='test4', type="test",
        #                     object_id=None, user_id=user1.id,)

        # queryset = Baby.objects.all()
        # queryset = Baby.prefetch_type_object(queryset)
        # queryset = Baby.load_user(queryset)
        # assert hasattr(queryset[0], 'type_object')
