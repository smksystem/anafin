# Generated by Django 2.0.4 on 2019-06-28 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0012_keepconfig_firstbuystate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keepconfig',
            old_name='firstbuystate',
            new_name='firstbuyflag',
        ),
    ]
