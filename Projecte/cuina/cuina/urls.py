from django.urls import path
from . import views

urlpatterns = [
    
    # url app, importem funció, name nom de referència a la ruta més fàcil de gestionar per canvis
    path("", views.home, name="home"),
   
    path("tags", views.tags, name="tags"),
    
    # del específic al general!!!! si poso paràmetre aquesta té més força que la genèrica!!!
    path("if/<str:nom>", views.condicional, name="if"),
    path("if", views.condicional, name="if"),
    
    path("for", views.bucle, name="for"),
    
    path("herencia", views.herencia, name="herencia"),
    
    path("errors/<str:nom>", views.errors, name="fallo"),
    path("errors", views.errors, name="fallo"),

]