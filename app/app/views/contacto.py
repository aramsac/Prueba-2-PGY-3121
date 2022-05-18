from django.shortcuts import render
def contacto_index(request):
    return render(request, 'contacto.html',{'aa': ' inh 1s', 'bb':123213})