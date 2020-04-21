from django.forms import ModelForm
from users.models import *

class Form(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user_id', 'user_password', 'user_name']