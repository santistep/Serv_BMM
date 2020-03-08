from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_usuario(request):
    return HttpResponse('Index Usuario')
