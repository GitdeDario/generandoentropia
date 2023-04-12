from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("losMalosTenianRazon", views.losMalosTenianRazon, name="losMalosTenianRazon"),
    path("miscosas", views.miscosas, name="miscosas"),
    path("loquenosepuededecir", views.loquenosepuededecir, name="loquenosepuededecir"),
    path("aikalaperra", views.aikalaperra, name="aikalaperra"),
    path("loquenosepuededecirLogueado", views.loquenosepuededecirLogueado, name="loquenosepuededecirLogueado"),
    path("logout",views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("estroncio", views.estroncio, name="estroncio"),
    path("reactorArk", views.reactorArk, name="reactorArk"),
    path("ardupiano", views.eNanoPiano, name="eNanoPiano"),
    path("numeros_IA", views.numeros_IA, name="numeros_IA"),
    #https://www.hackster.io/adhyoksh/controlling-gpio-pins-of-raspberry-pi-with-web-page-2d5bdc
    path("led1on", views.led1on, name="led1on"),
    path("led1off", views.led1off, name="led1off"),
]