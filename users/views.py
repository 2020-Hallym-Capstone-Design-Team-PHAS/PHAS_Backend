from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseForbidden, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from users.forms import *
from django.utils.encoding import smart_str
import bcrypt
import json


# Create your views here.

@csrf_exempt
def userRegist(request):
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            hashed_password = bcrypt.hashpw(json_data['user_password'].encode('utf-8'), bcrypt.gensalt()).decode()
            user_data = UserInfo(user_name=json_data['user_name'], user_password=hashed_password, user_id=json_data['user_id'])
            user_data.save()
            return HttpResponse()
        else:
            return HttpResponseNotAllowed("허용하지 않은 Http method 입니다.") #Http status 403
    except Exception as e:
        return HttpResponseServerError(user_data)


@csrf_exempt
def userSignIn(request):
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            selectedUserData = UserInfo.objects.filter(user_id__exact=json_data['user_id'])[0]
            if bcrypt.checkpw(json_data['user_password'].encode('utf-8'), selectedUserData.user_password.encode('utf-8')):
                return HttpResponse()
            else:
                return HttpResponseForbidden()
    except Exception as e:
        return HttpResponseServerError(e)
