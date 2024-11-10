from django.db import models
from users.models import User

class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def room_messages(self):
        return Message.objects.filter(room=self)
    
    def create_room_message(self,sender,message):
        new = Message(room=self,sender=sender,message=message)
        new.save()

    def __str__(self):
        return f'room: {self.room_name}'

class Message(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'user: {self.sender} && room: {self.room.room_name} && message: {self.message}'
