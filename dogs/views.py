from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from dogs.models import DogInfo
from .forms import DogForm
from django.views.decorators.csrf import csrf_exempt
from users.models import UserInfo as us
# Create your views here.

@csrf_exempt
def dogRegist(request):
    try:
        if request.method == 'POST':
            if DogInfo.objects.filter(Q(user_id=request.POST['user_id']) & Q(dog_name=request.POST['dog_name'])):
                return HttpResponse("이미 있는 정보")
            dogdata = DogInfo.objects.create(user_id = us.objects.get(user_id=request.POST['user_id']),
                                             dog_name = request.POST['dog_name'],
                                             dog_breed = request.POST['dog_breed'],
                                             dog_size = request.POST['dog_size'],
                                             dog_birth = request.POST['dog_birth'])
            return HttpResponse("입력완료")
            #if diform.is_valid():
            #    diform.save()
            #    return HttpResponse("입력 성공")#Http status 200
        else:
            #diform = DogForm
            return HttpResponse("허용하지 않은 Http method 입니다.") #Http status 403
    except Exception as e:
        return HttpResponse(e, " : Error 입니다.")
def dogInfo(request):
    return HttpResponse("dog info")