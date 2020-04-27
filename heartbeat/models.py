from django.db import models

# Create your models here.
class heartbeat(models.Model):
    audio_idx = models.AutoField(primary_key = True)
    user_id = models.CharField(max_length=64)
    dog_idx = models.IntegerField()
    audio_file_path = models.CharField(max_length=512)
    create_date = models.DateTimeField(auto_now_add=True)
    heartbeat_normal_condition = models.IntegerField()
    audio_file = models.FileField(blank=False,null=False)
