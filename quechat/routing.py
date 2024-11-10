from django.urls import path
from .consumers import ConsumerSocket

ws_urlpatterns = [
    path('ws/chat/<str:room_name>/',ConsumerSocket.as_asgi())
]