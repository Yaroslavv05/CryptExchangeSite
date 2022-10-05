from django.forms import ModelForm, TextInput, ValidationError
from .models import Task
import re


class Form(ModelForm):
    class Meta:
        model = Task
        fields = ['colvo_coin', 'Email', 'fio', 'num_wallet']
        widgets = {
            "colvo_coin": TextInput(attrs={
                'type': 'text',
                'id': 'from_summ',
                'name': 'Orders[summ_from]',
                'data-min': '0.12',
                'class': 'form-control'
            }),
            "Email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }),
            "fio": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО получателя'
            }),
            "num_wallet": TextInput(attrs={
                'class': 'form-control',
                'id': 'account'
            }),
        }
