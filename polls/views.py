from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def faq(request):
    return render(request, 'faq.html')


def catalog(request):
    return render(request, 'goods.html')


def cards_catalog(request):
    return render(request, 'card-good.html')
