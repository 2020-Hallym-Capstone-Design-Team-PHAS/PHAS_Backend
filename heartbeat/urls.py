from django.urls import path
from heartbeat.views import *

urlpatterns = [
    path("save", save_audio_file, name = "save Audio File"),
    path("search/log", search_log, name = "search Log")
]