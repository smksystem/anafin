# Generated by Django 2.0.4 on 2019-06-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0011_auto_20190401_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='keepconfig',
            name='firstbuystate',
            field=models.CharField(default='YES', max_length=3),
        ),
    ]
