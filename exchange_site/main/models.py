from django.db import models


class Task(models.Model):
    COLOR_CHOICES = (
        ('bitcoin', 'BTC'),
        ('riple', 'XRP'),)
    choise_coin = models.CharField(max_length=255, choices=COLOR_CHOICES, default='bitcoin')
    colvo_coin = models.CharField('Количество монет', max_length=10)
    Email = models.CharField('Почта', max_length=50)
    fio = models.CharField('ФИО', max_length=50)
    num_wallet = models.CharField('Номер кошелька:', max_length=30)

    def __str__(self):
        return self.colvo_coin