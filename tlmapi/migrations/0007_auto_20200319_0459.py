# Generated by Django 2.2.11 on 2020-03-19 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlmapi', '0006_auto_20200319_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformer',
            name='deviceid',
            field=models.CharField(blank=True, default='pv01', max_length=200),
        ),
        migrations.AlterField(
            model_name='transformer',
            name='pub_time',
            field=models.CharField(blank=True, default='time', max_length=200),
        ),
    ]
