from django.shortcuts import render

def index(request):
    return render(request, 'main/NETEX 24.html')


def create(request):
    return render(request, 'main/create.html')


def questions_and_answers(request):
    return render(request, 'main/Questions and answers.html')


def rules(request):
    return render(request, 'main/Rules.html')


def contact(request):
    return render(request, 'main/Contact.html')