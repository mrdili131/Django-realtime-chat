import json
from .models import  Room, Message
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from users.models import User

class ConsumerSocket(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        # Retrieve or create the room instance
        room = await self.get_room(self.room_name)
        
        # Save the message to the database
        await self.save_message(room, username, message)

        # Broadcast the message to the WebSocket group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "sendMessage",
                "message": message,
                "username": username,
            }
        )

    @database_sync_to_async
    def get_room(self, room_name):
        room, created = Room.objects.get_or_create(room_name=room_name)
        return room

    @database_sync_to_async
    def save_message(self, room, username, message):
        user = User.objects.get(username=username)
        Message.objects.create(room=room, sender=user, message=message)

    async def sendMessage(self,event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({"message":message,"username":username}))
