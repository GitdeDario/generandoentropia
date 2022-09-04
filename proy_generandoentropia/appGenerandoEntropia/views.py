import re
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import User

LED = 22
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.output(LED, 0)

# Create your views here.
def index(request):
    return render(request, "appGenerandoEntropia/index.html")

def chiste(request):
    return render(request, "appGenerandoEntropia/chiste.html")

def miscosas(request):
    return render(request, "appGenerandoEntropia/miscosas.html")

def estroncio(request):
    return render(request, "appGenerandoEntropia/estroncio.html")

def reactorArk(request):
    return render(request, "appGenerandoEntropia/reactorArk.html")

def amigurumis(request):
    return render(request, "appGenerandoEntropia/amigurumis.html")

def loquenosepuededecir(request):
    #return render(request, "appGenerandoEntropia/loquenosepuededecir.html")
    if request.method == "POST":
        #Lee lo que se haya escrito en los campos del form
        username = request.POST["username"]
        password = request.POST["password"]

        #Verifica si usuario y contraseña son correctos (los ingresados en el form)
        user = authenticate(request, username=username, password=password)

        #Si se devuelve un objeto USER, se puede loguear y se rutea a la pagina loquenosepuededecirLogueado
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("loquenosepuededecirLogueado"))
        #Si el usuario y/o contraseña no son correctos, nos redirige a la página para loguearnos, con un mensaje del error
        else:
            return render(request, "appGenerandoEntropia/loquenosepuededecir.html", {
                "message": "usuario y/o contraseña inválido"
            })

    return render(request, "appGenerandoEntropia/loquenosepuededecir.html")    

def loquenosepuededecirLogueado(request):
    #return render(request, "appGenerandoEntropia/loquenosepuededecirLogueado.html")
    # If no user is signed in, return to login page:     
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("loquenosepuededecir"))
    return render(request, "appGenerandoEntropia/loquenosepuededecirLogueado.html")
def led1on():
    GPIO.output(LED,1)
    return render(request, "appGenerandoEntropia/loquenosepuededecirLogueado.html")

def logout_view(request):
    logout(request)
    return render(request, "appGenerandoEntropia/logout.html")

def aikalaperra(request):
    return render(request, "appGenerandoEntropia/aikalaperra.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]      

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "appGenerandoEntropia/register.html", {
                "message": "Las contraseñas no son iguales."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "appGenerandoEntropia/register.html", {
                "message": "El usuario ya existe."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("loquenosepuededecirLogueado"))
    else:
        return render(request, "appGenerandoEntropia/register.html")