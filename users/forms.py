from django.forms import *
from users.models import *


class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('user_id', 'user_password', 'user_name')
