# Generated by Django 3.0.6 on 2020-10-04 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201004_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweeter',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 16, 36, 43, 996645), verbose_name='Дата создания'),
        ),
    ]
