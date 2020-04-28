from django.shortcuts import render
from heartbeat.models import Heartbeat
from django.http import *
from datetime import datetime
from heartbeat.forms import HeartBeatForm
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage


@csrf_exempt
def save_audio_file(request):
    try:
        if request.method == "POST":
            audio_data = HeartBeatForm(request.POST)
            if audio_data.is_valid() and request.FILES['audio_file']:
                obj = audio_data.save(commit=False)
                obj.audio_file = request.FILES['audio_file']
                obj.heartbeat_normal_condition = -1
                obj.save()
                return HttpResponse()
            else:
                return HttpResponseForbidden(audio_data)
        else:
            return HttpResponseNotAllowed()
    except Exception as e:
        return HttpResponseServerError(e)
