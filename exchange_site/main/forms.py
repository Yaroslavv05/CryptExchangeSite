from django.forms import ModelForm, TextInput, Select
from .models import Task

#gg
class Form(ModelForm):
    test = {
        'coin_name': 'Orders[currency_from]'
    }

    def add_prefix(self, field_name):
        field_name = self.test.get(field_name, field_name)
        return super(Form, self).add_prefix(field_name)

    class Meta:
        model = Task
        fields = ['colvo_coin', 'Email', 'fio', 'num_wallet', 'coin_name']
        widgets = {
            "coin_name": TextInput(attrs={
                'type': 'hidden',
                'value': '6',
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