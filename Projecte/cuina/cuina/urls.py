from django.urls import path
from . import views

urlpatterns = [
    # url app, importem funció, name nom de referència a la ruta més fàcil de gestionar per canvis
    path("home", views.home, name="home"),
   
    path("introduirrecepta", views.introduirrecepta, name="introduirrecepta"),
    
    # del específic al general!!!! si poso paràmetre aquesta té més força que la genèrica!!!
    path("login", views.login, name="login"),
    path("receptes", views.receptes, name="receptes"),
    
    path("register", views.register, name="register"),
    
    path("faqs", views.faqs, name="faqs"),
    
    path("contact", views.contact, name="contact"),
]