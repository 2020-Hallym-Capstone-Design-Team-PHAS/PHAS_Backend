from django.urls import path
from users.views import *

urlpatterns = [
    path('regist', userRegist, name = "user_regist"),
    path('sign-in', userSignIn, name = "user_signIn")
]