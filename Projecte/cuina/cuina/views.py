from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from datetime import date

#! PRIMER CAL RECORDAR CRTL+F5 PER ACTUALITZAR CACHÉ DEL NAVEGADOR

def home(request):
    return render(request, 'vistes_templates/home.html')

def introduirrecepta(request):
    return render(request, 'vistes_templates/introduirrecepta.html')

def login (request):
    return render(request, 'vistes_templates/login.html')

def receptes (request):
    return render(request, 'vistes_templates/receptes.html')

def register (request):
    return render(request, 'vistes_templates/register.html')

def faqs (request):
    return render(request, 'vistes_templates/faqs.html')

def contact (request):
    return render(request, 'vistes_templates/contact.html')