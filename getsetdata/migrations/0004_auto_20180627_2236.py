# Generated by Django 2.0.4 on 2018-06-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getsetdata', '0003_auto_20180616_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hlfinstatisticasof',
            name='lastprice',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='hlfinstatisticasof',
            name='marketcap',
            field=models.FloatField(),
        ),
    ]
