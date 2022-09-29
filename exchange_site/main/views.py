from django.shortcuts import render


def index(request):
    return render(request, 'main/NETEX 24.html')


def create(request):
    return render(request, 'main/create.html')