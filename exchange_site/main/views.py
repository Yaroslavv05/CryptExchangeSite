from django.shortcuts import render
from .forms import Form

def index(request):
    return render(request, 'main/NETEX 24.html')


def create(request):
    form =  Form()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def questions_and_answers(request):
    return render(request, 'main/Questions and answers.html')


def rules(request):
    return render(request, 'main/rules.html')


def contact(request):
    return render(request, 'main/contacts.html')