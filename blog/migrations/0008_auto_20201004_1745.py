# Generated by Django 3.0.6 on 2020-10-04 11:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20201004_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweeter',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tweet', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='tweeter',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 17, 45, 36, 796653), verbose_name='Дата создания'),
        ),
    ]
