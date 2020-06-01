from django.http import *
from heartbeat.models import Heartbeat
from heartbeat.forms import HeartBeatForm
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime



@csrf_exempt
def save_audio_file(request):
    try:
        if request.method == "POST":
            json_data = json.dumps(request.body)
            audio_data = HeartBeatForm(json_data)
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

