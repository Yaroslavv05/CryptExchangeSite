from django.shortcuts import render
from .forms import Form
from django.contrib import messages
from django.shortcuts import redirect
def index(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
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