from django.http import JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def home(request):
    return render(request, 'dojo/index.html')


def session(request, session_id):
    pilot = request.GET.get('pilot', False)
    return render(request, 'dojo/session.html', {
        'session_id': mark_safe(json.dumps(session_id)),
        'pilot': mark_safe(json.dumps(pilot)),
    })
