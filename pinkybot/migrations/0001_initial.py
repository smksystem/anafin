# Generated by Django 2.0.4 on 2019-02-04 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='monitorbidoffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mastershare', models.CharField(default='', max_length=50)),
                ('timestamp', models.DateTimeField(verbose_name=0)),
                ('bid1', models.FloatField()),
                ('offer1', models.FloatField()),
                ('bidvolumn1', models.FloatField()),
                ('offervolumn1', models.FloatField()),
                ('bid2', models.FloatField()),
                ('offer2', models.FloatField()),
                ('bidvolumn2', models.FloatField()),
                ('offervolumn2', models.FloatField()),
                ('bid3', models.FloatField()),
                ('offer3', models.FloatField()),
                ('bidvolumn3', models.FloatField()),
                ('offervolumn3', models.FloatField()),
                ('bid4', models.FloatField()),
                ('offer4', models.FloatField()),
                ('bidvolumn4', models.FloatField()),
                ('offervolumn4', models.FloatField()),
                ('bid5', models.FloatField()),
                ('offer5', models.FloatField()),
                ('bidvolumn5', models.FloatField()),
                ('offervolumn5', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='udpatestockvalue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuefield', models.CharField(default='', max_length=10)),
                ('datefield', models.DateTimeField(verbose_name=0)),
                ('timefield', models.DateTimeField(verbose_name=0)),
                ('orderfield', models.CharField(default='', max_length=5)),
                ('statusfield', models.CharField(default='', max_length=20)),
                ('volumnfield', models.CharField(default='', max_length=10)),
                ('buyfield', models.CharField(default='', max_length=5)),
                ('sellfield', models.CharField(default='', max_length=5)),
                ('cancelfield', models.CharField(default='', max_length=5)),
                ('targetvalue', models.CharField(default='', max_length=10)),
                ('profitfield', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='updaterefresh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.CharField(default='', max_length=10)),
                ('time', models.CharField(default='', max_length=10)),
                ('symbole', models.CharField(default='', max_length=10)),
                ('side', models.CharField(default='', max_length=3)),
                ('price', models.CharField(default='', max_length=10)),
                ('volume', models.CharField(default='', max_length=10)),
                ('matched', models.CharField(default='', max_length=10)),
                ('balance', models.CharField(default='', max_length=10)),
                ('cancelled', models.CharField(default='', max_length=10)),
                ('status', models.CharField(default='', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('matchedtime', models.CharField(default='-', max_length=10)),
                ('referorderfrom', models.CharField(default='-', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='valuechange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datefield', models.DateField(verbose_name=0)),
                ('timestamp', models.TimeField(verbose_name=0)),
                ('stockname', models.CharField(max_length=10)),
                ('stockvalue', models.CharField(default='', max_length=5)),
                ('totalvolume', models.CharField(default='', max_length=15)),
                ('totalvolue', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
