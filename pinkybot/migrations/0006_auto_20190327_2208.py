# Generated by Django 2.0.4 on 2019-03-27 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0005_keepconfig_planvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keepconfig',
            name='source',
            field=models.CharField(default='', max_length=30),
        ),
    ]
