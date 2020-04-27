from django.db import models
import users.models as us
# Create your models here.
class DogInfo(models.Model):
    user_id = models.ForeignKey(us.UserInfo, on_delete=models.CASCADE)
    dog_idx = models.AutoField(primary_key=True)
    dog_breed = models.CharField(max_length=64)
    dog_name = models.CharField(max_length=32)
    dog_size = models.PositiveSmallIntegerField()
    dog_birth = models.DateTimeField()
    create_date = models.DateField(auto_now_add=True)