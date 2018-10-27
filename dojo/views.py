from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def home(request):
    return render(request, 'dojo/index.html')


def session(request, session_id):
    return render(request, 'dojo/session.html', {
        'session_id': mark_safe(json.dumps(session_id))
    })

