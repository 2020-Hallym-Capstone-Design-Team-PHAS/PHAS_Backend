# Generated by Django 3.0.5 on 2020-04-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200420_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_data',
            field=models.DateField(auto_now_add=True),
        ),
    ]