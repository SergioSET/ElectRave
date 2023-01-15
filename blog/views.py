from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "ElectRave user page",
        },
    )

def gestion_usuario(request):
    return render(request, 'gestion_usuarios.html')