from django.urls import path
from . import views

urlpatterns = [
    path('',views.CreateRoomView.as_view(),name='home'),
    path('message/<str:room_name>/',views.MessageView,name='message')
]
