# Generated by Django 2.0.4 on 2019-07-04 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0015_auto_20190703_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='keeplogin',
            name='profileId',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='keeplogin',
            name='pinId',
            field=models.CharField(default='', max_length=12),
        ),
    ]