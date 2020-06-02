from django.db import models


# Create your models here.
class Heartbeat(models.Model):
    audio_idx = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=64)
    dog_name = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    heartbeat_normal_condition = models.IntegerField(null=True)
    audio_file = models.FileField()
