from django.shortcuts import render
from .models import Login
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