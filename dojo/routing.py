from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/session/<session_id>/', consumers.SessionConsumer),
]
