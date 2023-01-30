from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import User

# Create your views here.

@login_required

def home(request):
    return render(request, 'home.html')

def index(request):
    use = User.objects.all()        
    context={"title": "ElectRave user page",'use': use}
    return render(request,"index.html",context
    )

def gestion_usuario(request):
    return render(request, 'listaUsuarios.html')