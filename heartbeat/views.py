from django.http import *
from heartbeat.models import Heartbeat
from heartbeat.forms import HeartBeatForm
from django.views.decorators.csrf import csrf_exempt
from heartbeat.PhasNoiseReduce import noiseReduce
import json
from datetime import datetime
import logging
import os
import sys
import time

@csrf_exempt
def save_audio_file(request):
    try:
        if request.method == "POST":

            audio_data = HeartBeatForm(request.POST, request.FILES)
            

            if audio_data.is_valid():
                file_name_rebase = audio_data.cleaned_data['user_id'] + \
                                   '_' + audio_data.cleaned_data['dog_name'] + \
                                   '_' + datetime.now().strftime("%Y-%m-%d_%H시:%M분") + \
                                   '.aac'
                
                obj = Heartbeat(user_id=audio_data.cleaned_data['user_id'],
                                dog_name=audio_data.cleaned_data['dog_name'])
                obj.audio_file = request.FILES['audio_file']
                obj.audio_file.name = file_name_rebase
                obj.heartbeat_normal_condition = -1
                obj.save()
                
                os.system('ffmpeg -i ./heartbeat_data/' + obj.audio_file.name + ' ' + './heartbeat_data/' + obj.audio_file.name[:-4] + '.wav')
                os.system('rm -r ./heartbeat_data/'+ obj.audio_file.name)
                
                noiseReduce(obj.audio_file.name[:-4])

                return HttpResponse()
            else:
                return HttpResponseForbidden(request.FILES['audio_file'])
        else:
            return HttpResponseNotAllowed()
    except Exception as e:
        return HttpResponseServerError(e)


@csrf_exempt
def search_log(request):
    try:
        if request.method == "POST":
            json_data = json.loads(request.body)
            audio_info = Heartbeat.objects.filter(audio_idx__exact=json_data['audio_idx'])[0]
            audio_info_dic = {
                              "audio_idx":audio_info.audio_idx,
                              "dog_name":audio_info.dog_name,
                              "user_id" : audio_info.user_id,
                              "create_data":json_default(audio_info.create_date),
                              "heartbeat_normal_condition":audio_info.heartbeat_normal_condition
                              }
            return HttpResponse(json.dumps(audio_info_dic))
        else:
            return HttpResponseForbidden()
    except Exception as e:
        return HttpResponseServerError(e)


def json_default(value):
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%d_%H:%M')

