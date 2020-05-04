from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_id = models.CharField(max_length=128, primary_key=True, null=False)
    user_password = models.CharField(max_length=128, null=False)
    user_name = models.CharField(max_length=32, null=False)
    create_data = models.DateField(auto_now_add=True, null=False)

