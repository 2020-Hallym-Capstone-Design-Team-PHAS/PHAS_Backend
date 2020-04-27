from django.urls import path
from heartbeat.views import *

urlpatterns = [
    path("save", saveAudioFile, name = "save Audio File")

]