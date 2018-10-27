from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def home(request):
    return render(request, 'dojo/index.html')


def chat(request):
    return render(request, 'dojo/chat.html')


def room(request, room_name):
    return render(request, 'dojo/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

