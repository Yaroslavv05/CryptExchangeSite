# Generated by Django 4.1.1 on 2022-10-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_task_choise_coin'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='coin_name',
            field=models.CharField(default=1, max_length=30, verbose_name='Название монеты'),
            preserve_default=False,
        ),
    ]
