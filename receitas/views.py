from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render (request, 'receitas/pages/home.html', context={'name': 'Leandro França' })

def receitas(request, id):
    return render (request, 'receitas/pages/receitas-view.html', context={'name': 'Leandro França' })




