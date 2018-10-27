from django.http import JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def home(request):
    return render(request, 'dojo/index.html')


def session(request, session_id):
    code = ""
    tests = ""
    output = ""
    currentStep = "red"
    pilot = request.GET.get('pilot', "") == "true"
    return render(request, 'dojo/session.html', {
        'session_id': mark_safe(json.dumps(session_id)),
        'code': mark_safe(json.dumps(code)),
        'tests': mark_safe(json.dumps(tests)),
        'output': mark_safe(json.dumps(output)),
        'currentStep': mark_safe(json.dumps(currentStep)),
        'pilot': mark_safe(json.dumps(pilot)),
    })
