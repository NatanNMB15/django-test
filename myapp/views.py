from django.shortcuts import render, redirect
from .models import Login
from .form import LoginForm
import datetime

def home(request):

    data = {}

    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'myapp/home.html', data)

def listagem(request):
    data = {}
    data['contas'] = Login.objects.all()

    return render(request, 'myapp/listagem.html', data)

def novo_Login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    return render(request, 'myapp/form.html', {'form':form})

def atualizar_Login(request, pk):
    login = Login.objects.get(pk=pk)
    form = LoginForm(request.POST or None, instance=login)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    return render(request, 'myapp/form.html', {'form':form, 'login':login})

def excluir_Login(request, pk):
    login = Login.objects.get(pk=pk)
    login.delete()
    return redirect('listagem')