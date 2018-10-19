from django.shortcuts import render


def home(request):
    return render(request, 'dojo/index.html')
