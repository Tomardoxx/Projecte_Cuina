from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from datetime import date

#! PRIMER CAL RECORDAR CRTL+F5 PER ACTUALITZAR CACHÉ DEL NAVEGADOR

def home(request):
    
    # render (petició url, resposta servidor(nom_template), diccionari per fer la crida dels tags)
    # reverse (name url que agafa la ruta i li donem dinamisme)
    pagines=[
        
        {
            "nom":"tags",
            "url":reverse("tags"),
        },
        
        {
            "nom":"if",
            "url":reverse("if"),
        },
        
         {
            "nom":"for",
            "url":reverse("for"),
        },      
        
        {
            "nom":"herència",
            "url":reverse("herencia"),
        },  
        
         {
            "nom":"errors",
            "url":reverse("fallo"),
        },          
    ]
    
    return render(request, 'vistes_templates/index.html', {"pagines":pagines})


#? passar diccionari render, fer la crida al dict i tags ---------------------------------------------------

def tags(request):
    
    data=date.today()
    
    return render(request, 'vistes_templates/tags.html', {"nom":"Son Goku",
                                         "data": data})
    
#? tag condicional per template -----------------------------------------------------------------

# paràmetre definit com a buit per pàgina general, fem treballar el template si passem un paràmetre
def condicional(request, nom=""):
    
    return render(request, 'vistes_templates/if.html', {"nom": nom})

#? tag for per template -------------------------------------------------------

def bucle(request):
    
    escola_tortuga={
        
        "alumne1":{
            "nom": "Son Goku",
            "edat": 43,
            "attack": "Kame-Ha"
        },
        
        "alumne2":{
            "nom": "Krilin",
            "edat": 44,
            "attack": "Kienzan"
        },
        
        "alumne3":{
            "nom": "Yamcha",
            "edat": 45,
            "attack": "Sokidan"
        },
        
    }
    
    return render(request, 'vistes_templates/for.html', {"escola":escola_tortuga})

#? herència template -------------------------------------------------------------------------------

def herencia(request):
    
    return render(request, 'vistes_templates/herencia.html')

#? utilitzar el 404 per errors de servidors (mode developer) ------------------------------------------------------------

def errors(request, nom=""):
    
    valors={
        
        "guts":"https://m.media-amazon.com/images/I/81YFvUrchWL._UF894,1000_QL80_.jpg",
        "caska":"https://upload.wikimedia.org/wikipedia/it/thumb/b/b5/Caska.png/1200px-Caska.png",
        "griffith":"https://i.pinimg.com/736x/69/1d/cb/691dcbc2bbcf6a9caf39557fb8ef59c9.jpg",
        "puck": "https://i.pinimg.com/736x/6f/20/71/6f20718f5c58b30ed1047aef4e0d1c29.jpg",
        
    }
    
    if not nom:
        return render(request, 'vistes_templates/errors.html')
        
    nom=nom.lower()
    
    imatge=valors.get(nom)
    
    if not imatge:
        return render(request, 'vistes_templates/404.html')
    
    return render(request, 'vistes_templates/errors.html', {"imatge":imatge, "nom":nom})