# Generated by Django 2.1 on 2018-06-13 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComSetName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_id', models.IntegerField(unique=True)),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('fullname', models.TextField(blank=True, null=True)),
                ('market', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='HLFinPeriodasof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mastershare', models.CharField(default='', max_length=50, unique=True)),
                ('assets', models.FloatField(default=0)),
                ('liabilities', models.FloatField()),
                ('equity', models.FloatField()),
                ('paidcapital', models.FloatField()),
                ('revenue', models.FloatField()),
                ('netprofit', models.FloatField()),
                ('epsbath', models.FloatField()),
                ('roa', models.FloatField()),
                ('roe', models.FloatField()),
                ('netprofitmargin', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HLFinStatisticasof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mastershare', models.CharField(default='', max_length=50, unique=True)),
                ('lastprice', models.FloatField()),
                ('marketcap', models.FloatField()),
                ('fsperiodasof', models.CharField(max_length=50)),
                ('p_e', models.FloatField()),
                ('p_bv', models.FloatField()),
                ('bookvaluepershare', models.FloatField()),
                ('dvdyield', models.FloatField()),
            ],
        ),
    ]
