from django.contrib import admin

# Register your models here.
from .models import DogInfo

admin.site.register(DogInfo)