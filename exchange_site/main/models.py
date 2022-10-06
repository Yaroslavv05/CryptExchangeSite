from django.db import models


class Task(models.Model):
    colvo_coin = models.CharField('Количество монет', max_length=10)
    Email = models.CharField('Почта', max_length=50)
    fio = models.CharField('ФИО', max_length=50)
    num_wallet = models.CharField('Номер кошелька:', max_length=30)
    coin_name = models.CharField('Название монеты', max_length=30)

    def __str__(self):
        return self.colvo_coin