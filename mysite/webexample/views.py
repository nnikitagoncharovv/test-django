from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h3>Привет мир! Как жизнь? Чего как?</h3>')
