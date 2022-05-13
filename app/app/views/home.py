from django.shortcuts import render

def index(request):
    return render(request, 'index.html',{'a': 'prueba parametros', 'b':1})
