# Generated by Django 2.0.4 on 2019-08-10 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0025_auto_20190809_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keepconfig',
            old_name='totalvaluebuy',
            new_name='totalcostbuy',
        ),
    ]
