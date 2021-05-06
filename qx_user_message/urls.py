from django.urls import path, include
from rest_framework.routers import DefaultRouter
from qx_user_message.viewsets import UserMessageViewSet


router = DefaultRouter()
router.register('user-message', UserMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
