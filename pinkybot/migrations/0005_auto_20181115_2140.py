# Generated by Django 2.0.4 on 2018-11-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0004_auto_20181114_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='udpatestockvalue',
            name='statusfield',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='updaterefresh',
            name='status',
            field=models.CharField(default='', max_length=20),
        ),
    ]
