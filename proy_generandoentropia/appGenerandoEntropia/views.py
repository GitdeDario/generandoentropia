import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "appGenerandoEntropia/index.html")

def chiste(request):
    return render(request, "appGenerandoEntropia/chiste.html")

def miscosas(request):
    return render(request, "appGenerandoEntropia/miscosas.html")

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

def logout_view(request):
    logout(request)
    return render(request, "appGenerandoEntropia/logout.html")

def aikalaperra(request):
    return render(request, "appGenerandoEntropia/aikalaperra.html")

