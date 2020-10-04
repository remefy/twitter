from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Model
from django.db import models


class Tweeter(Model):
    created_date = models.DateTimeField(verbose_name='Дата создания', default=datetime.now())
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, related_name='tweet')
    text = models.CharField(verbose_name='Текст сообщения', max_length=250)
    likes = models.IntegerField(verbose_name='Количество лайков', default=0)

    class Meta:
        verbose_name_plural = 'Твиты'
        verbose_name = 'Твит'

    def __str__(self):
        return self.text

