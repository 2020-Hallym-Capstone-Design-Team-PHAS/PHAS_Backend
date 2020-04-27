from django.forms import ModelForm
from django import forms
from heartbeat.models import *


class Form(forms.ModelForm):
    class Meta:
        model = heartbeat
        fields = ['user_id', 'dog_idx']
