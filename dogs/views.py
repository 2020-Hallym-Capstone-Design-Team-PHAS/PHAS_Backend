from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dogRegist(request):
    return HttpResponse("Rgst dog")

def dogInfo(request):
    return HttpResponse("dog info")