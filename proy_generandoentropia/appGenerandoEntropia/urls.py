from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chiste", views.chiste, name="chiste"),
    path("miscosas", views.miscosas, name="miscosas"),
    path("loquenosepuededecir", views.loquenosepuededecir, name="loquenosepuededecir"),
    path("aikalaperra", views.aikalaperra, name="aikalaperra"),
]