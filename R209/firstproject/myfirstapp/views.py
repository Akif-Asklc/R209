from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myfirstapp/index.html')

def seconde(request):
    return render(request, 'myfirstapp/seconde.html')

def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')