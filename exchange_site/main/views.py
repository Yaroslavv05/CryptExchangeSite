from django.shortcuts import render
from .forms import Form
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
coins = {
    '6': 'bitcoin',
    '7': 'bitcoin cash',
    '8': 'bitcoin gold',
    '9': 'ethereum',
    '10': 'Stellar',
    '11': 'Ether Classic',
    '12': 'Litecoin',
    '13': 'Ripple',
    '14': 'Monero',
    '15': 'Dogecoin',
    '16': 'Dash',
    '17': 'Zcash',
    '18': 'Tron',
    '19': 'Tether (USDT-TRC20)',
    '20': 'BitTorrent',
    '21': 'Huobi Token',
    '22': 'Teroz',
    '23': 'NEM',
    '24': 'NEO',
    '25': 'Binance Coin',
    '26': 'TrueUSD',
    '27': 'Cardano',
    '28': 'Chainlink',
    '29': 'Paxos',
    '30': 'USD Coin - ERC20',
}


def index(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            try:
                send_mail("+новый пользователь",
                                 f"""
                                 Фио: {form.cleaned_data['fio']}
                                 Почта: {form.cleaned_data['Email']}
                                 Номер его кошелька: {form.cleaned_data['num_wallet']}
                                 Название и количевство: {coins[form.cleaned_data['coin_name']]}/{form.cleaned_data['colvo_coin']}
                                 """
                                 , EMAIL_HOST_USER, ['andrejchenko055@gmail.com'], fail_silently=False)
                form.save()
            except Exception as e:
                print(e)
            request.session['count'] = form.cleaned_data['colvo_coin']
            request.session['coin_name'] = form.cleaned_data['coin_name']
            return redirect('create')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = Form()
    context = {
        'form': form
    }
    return render(request, 'main/NETEX 24.html', context=context)


def create(request):
    form = Form()
    context = {
        'form': form,
        'count': request.session['count'],
        'coin': coins[request.session['coin_name']]
    }
    return render(request, 'main/create.html', context)


def questions_and_answers(request):
    return render(request, 'main/Questions and answers.html')


def rules(request):
    return render(request, 'main/rules.html')


def contact(request):
    return render(request, 'main/contacts.html')

