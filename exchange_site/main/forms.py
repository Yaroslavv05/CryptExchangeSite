from django.forms import ModelForm, TextInput, Select
from .models import Task
import re


class Form(ModelForm):
    class Meta:
        model = Task
        fields = ['choise_coin', 'colvo_coin', 'Email', 'fio', 'num_wallet']
        widgets = {
            "choise_coin": Select(attrs={
                'type': 'hidden',
                'name': 'Orders[currency_from]'
            }),
            "colvo_coin": TextInput(attrs={
                'type': 'text',
                'id': 'from_summ',
                'name': 'Orders[summ_from]',
                'data-min': '0.12',
                'class': 'form-control'
            }),
            "Email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
                'name': 'Orders[contact]'
            }),
            "fio": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО получателя',
                'name': 'Orders[fio]'
            }),
            "num_wallet": TextInput(attrs={
                'class': 'form-control',
                'id': 'account',
                'name': 'Orders[account]',
                'placeholder': 'Номер кошелька',
            }),
        }
