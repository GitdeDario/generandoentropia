import re
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "appGenerandoEntropia/index.html")

def chiste(request):
    return render(request, "appGenerandoEntropia/chiste.html")

def miscosas(request):
    return render(request, "appGenerandoEntropia/miscosas.html")

def loquenosepuededecir(request):
    return render(request, "appGenerandoEntropia/loquenosepuededecir.html")

def aikalaperra(request):
    return render(request, "appGenerandoEntropia/aikalaperra.html")