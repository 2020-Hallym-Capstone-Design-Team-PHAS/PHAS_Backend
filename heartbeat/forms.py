from django.forms import ModelForm
from django.forms import *
from heartbeat.models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
class HeartBeatForm(ModelForm):
    class Meta:
        model = Heartbeat
        fields = ['user_id', 'dog_name', 'audio_file']
