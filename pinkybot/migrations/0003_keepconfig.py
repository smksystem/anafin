# Generated by Django 2.1 on 2019-03-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinkybot', '0002_auto_20190222_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='keepconfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initinvest', models.CharField(default='', max_length=10)),
                ('volumestep', models.CharField(default='', max_length=5)),
                ('profitstep', models.CharField(default='', max_length=10)),
                ('topvaluerange', models.CharField(default='', max_length=5)),
                ('startvaluebuy', models.CharField(default='', max_length=5)),
                ('floorvaluerange', models.CharField(default='', max_length=5)),
                ('stopvaluerange', models.CharField(default='', max_length=5)),
                ('stockname', models.CharField(default='', max_length=10)),
            ],
        ),
    ]