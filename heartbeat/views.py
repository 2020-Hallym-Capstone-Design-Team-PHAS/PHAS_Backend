from django.shortcuts import render
from heartbeat.models import heartbeat
from django.http import *
from datetime import datetime
from heartbeat.forms import Form
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

@csrf_exempt
def saveAudioFile(request):
    try:
        if request.method == "POST":
            audio_data = Form(request.POST)
            if audio_data.is_valid() and request.FILES['audio_file']:
                obj = audio_data.save(commit=False)
                obj.audio_file_path = request.POST['user_id'] + '_' + request.POST['dog_idx'] + '_' + '{0:%Y_%m_%d %H:%M:%S}'.format(datetime.now()) + '_' + request.FILES['files'].name[-4:]
                obj.heartbeat_normal_condition = -1
                obj.save()
                return HttpResponse()
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseNotAllowed()
    except Exception as e:
        return HttpResponseServerError(e)
