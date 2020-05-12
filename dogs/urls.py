from django.urls import path

from dogs.views import *

urlpatterns = [
    path('dogregist', dogRegist, name = 'dog_regist'),
    path('doginfo_user', dogInfo_user, name = 'dog_info_user'),
    path('doginfo_dog', dogInfo_dog, name = 'dog_info_dog'),
    path('doginfo_del', dogInfo_del, name = 'dog_info_del'),

]