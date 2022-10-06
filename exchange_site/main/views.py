from django.shortcuts import render
from .forms import Form
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['coin_name'], form.cleaned_data['colvo_coin'], 'ggwp4117@ukr.net', ['chornyyaroslav5@gmail.com'], fail_silently=False)
            request.session['count'] = form.cleaned_data['colvo_coin']
            request.session['coin_name'] = form.cleaned_data['coin_name']
            form.save()
            print(mail)
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

