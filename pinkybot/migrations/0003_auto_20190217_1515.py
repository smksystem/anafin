# Generated by Django 2.0.4 on 2019-02-17 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0002_auto_20190205_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='updaterefresh',
            old_name='referorderfrom',
            new_name='referorderno',
        ),
    ]