# Generated by Django 2.1 on 2019-04-01 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0008_auto_20190401_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keepconfig',
            old_name='source',
            new_name='pluginfile',
        ),
    ]