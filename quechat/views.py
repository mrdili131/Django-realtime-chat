from django.shortcuts import render, redirect
from django.views import View
from .models import Room, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateRoomView(LoginRequiredMixin,View):
    def get(self,request):
        rooms = Room.objects.filter(message__sender=request.user).distinct()
        return render(request,'index.html',{"rooms":rooms})
    def post(self,request):
        room = request.POST['room_name']
        room = str(room).replace(" ","_")
        return redirect('message',room_name=room)
    
@login_required
def MessageView(request,room_name):
    user = request.user
    room, created = Room.objects.get_or_create(room_name=room_name)
    messages = Message.objects.filter(room=room).order_by('created_at')
    data = {
        "user":user,
        "messages":messages,
        "room":room
    }
    return render(request,'message.html',data)