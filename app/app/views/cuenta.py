from urllib3 import response
import requests

from django.shortcuts import render



def crear_usuario(request):
    print(request)
    return render(request , 'crear_usuario.html')
