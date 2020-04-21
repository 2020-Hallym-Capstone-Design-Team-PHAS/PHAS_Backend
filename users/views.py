from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseForbidden, HttpResponseServerError
from users.models import UserInfo
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from users.forms import *
import bcrypt

# Create your views here.

@csrf_exempt
def userRegist(request):
    try:
        if request.method == 'POST':
            hashedPassword = bcrypt.hashpw(request.POST['user_password'].encode('utf-8'), bcrypt.gensalt()).decode()
            userData = UserInfo(user_id=request.POST['user_id'], user_password=hashedPassword, user_name=request.POST['user_name'])
            userData.save()
            return HttpResponse() #Http status 200
        else:
            return HttpResponseNotAllowed("허용하지 않은 Http method 입니다.") #Http status 403
    except Exception as e:
        return  HttpResponse(e, " : Error 입니다.")


@csrf_exempt
def userSignIn(request):
    try:
        if request.method == 'POST':
            selectedUserData = UserInfo.objects.filter(user_id__exact=request.POST['user_id'])[0]
            if bcrypt.checkpw(request.POST['user_password'].encode('utf-8'), selectedUserData.user_password.encode('utf-8')):
                return HttpResponse()
            else:
                return HttpResponseForbidden()
    except Exception as e:
        return HttpResponseServerError(e)



