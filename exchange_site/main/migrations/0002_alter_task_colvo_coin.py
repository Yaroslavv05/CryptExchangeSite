# Generated by Django 4.1.1 on 2022-10-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='colvo_coin',
            field=models.CharField(blank=True, max_length=10, verbose_name='Количество монет'),
        ),
    ]