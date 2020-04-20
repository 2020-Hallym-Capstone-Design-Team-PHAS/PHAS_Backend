from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_id = models.CharField(max_length=128)
    user_password = models.CharField(max_length=128)
    user_name = models.CharField(max_length=32)
    create_data = models.DateField('date published')

