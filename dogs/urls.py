from django.urls import path

from dogs.views import *

urlpatterns = [
    path('dogregist', dogRegist, name = 'dog_regist'),
    path('doginfo', dogInfo, name = 'dog_info'),
]