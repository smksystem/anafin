# Generated by Django 2.0.4 on 2019-07-08 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0017_keeplogin_currentuseid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keeplogin',
            name='profileId',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
    ]
