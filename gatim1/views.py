from django.shortcuts import render
from .models import Retete

def index(request):
    return render(request, 'index.html', {})

# def retete(request):
#     return render(request, 'retete.html', {})

def condimente(request):
    return render(request, 'condimente.html', {})

def blog(request):
        return render(request, 'blog.html', {})

def retete(request):
    retete_ok = Retete.objects.all().order_by('date')
    return render(request, 'retete.html', {'retete_ok':retete_ok})