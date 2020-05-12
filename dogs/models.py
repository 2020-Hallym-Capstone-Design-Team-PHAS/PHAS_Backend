from django.db import models
import users.models as us
# Create your models here.
class DogInfo(models.Model):
    user_id = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE)
    dog_breed = models.CharField(max_length=64, null=True)
    dog_name = models.CharField(max_length=32, primary_key=True)
    dog_size = models.PositiveSmallIntegerField(null=True)
    dog_birth = models.DateField(null=True)
