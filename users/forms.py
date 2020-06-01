from django.forms import *
from users.models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('user_id', 'user_password', 'user_name')
