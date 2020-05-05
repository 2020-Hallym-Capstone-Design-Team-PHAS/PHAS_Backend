from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from dogs.models import DogInfo
from .forms import DogForm
from django.views.decorators.csrf import csrf_exempt
from users.models import UserInfo as us
import json
# Create your views here.

@csrf_exempt
def dogRegist(request):#강아지 정보 등록
    try:
        if request.method == 'POST':
            dog_json = json.loads(request.body)
            if DogInfo.objects.filter(Q(user_id=dog_json['user_id']) & Q(dog_name=dog_json['dog_name'])):
                return HttpResponse("이미 있는 정보")

            dogdata = DogInfo.objects.create(user_id = us.objects.get(user_id=dog_json['user_id']),
                                             dog_name = dog_json['dog_name'],
                                             dog_breed = dog_json['dog_breed'],
                                             dog_size = dog_json['dog_size'],
                                             dog_birth = dog_json['dog_birth'])
            result_data = {"result_code" : 1}
            return HttpResponse(json.dumps(result_data))
        else:
            return HttpResponse("허용하지 않은 Http method 입니다.") #Http status 403
    except Exception as e:
        return HttpResponse(e, " : Error 입니다.")

@csrf_exempt
def dogInfo_user(request):#사용자 보유 애완동물 목록
    try:
        if request.method == 'POST':
            dog_json = json.loads(request.body)
            s_data = DogInfo.objects.filter(Q(user_id=dog_json['user_id']))
            if s_data:

                return HttpResponse(s_data.values('dog_name'))
            else:
                return HttpResponse(json.dumps({"result_code" : 0}))
        else:
            return HttpResponse("허용하지 않은 Http method 입니다.")  # Http status 403
    except e:
        return HttpResponse(e, " : Error 입니다.")

@csrf_exempt
def dogInfo_dog(request):#사용자 보유 애완동물 상세정보
    try:
        if request.method == 'POST':
            dog_json = json.loads(request.body)
            s_data = DogInfo.objects.filter(Q(user_id=dog_json['user_id']) & Q(dog_name=dog_json['dog_name']))
            if s_data:
                return HttpResponse(s_data.values())
            else:
                return HttpResponse("해당 애완동물 정보 없음")
        else:
            # diform = DogForm
            return HttpResponse("허용하지 않은 Http method 입니다.")  # Http status 403
    except e:
        return HttpResponse(e, " : Error 입니다.")

@csrf_exempt
def dogInfo_del(request):#사용자 보유 애완동물 상세정보
    try:
        if request.method == 'POST':
            dog_json = json.loads(request.body)

            s_data = DogInfo.objects.filter(Q(user_id=dog_json['user_id']) & Q(dog_name=dog_json['dog_name']))
            if s_data:
                s_data.delete()
                return HttpResponse('삭제 완료')
            else:
                return HttpResponse("해당 애완동물 정보 없음")
        else:
            # diform = DogForm
            return HttpResponse("허용하지 않은 Http method 입니다.")  # Http status 403
    except e:
        return HttpResponse(e, " : Error 입니다.")