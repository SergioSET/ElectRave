from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import User, Factura
from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, 'home.html')

def index(request, id_usuario):
    usuari = User.objects.get(id=id_usuario)
    usuario = User.objects.get(id=id_usuario).username
    use = User.objects.all()   
    casillas = []
    fechas = []

    def get_graph():
        fac = Factura.objects.all()  
        tamaño = fac.latest('id').id
        for m in range(1, tamaño+1):
            if Factura.objects.filter(id=m).exists() :
                if Factura.objects.get(id=m).cliente == usuario:
                    casillas.append(float(fac.get(id=m).consumo))
                else:
                    print("")
            else:
                print("")
        return casillas

    def get_graph1():
        usuario = User.objects.get(id=id_usuario).username
        fac = Factura.objects.all()  
        tamaño = fac.latest('id').id
        for m in range(1, tamaño+1):
            if Factura.objects.filter(id=m).exists() :
                if Factura.objects.get(id=m).cliente == usuario:
                    fechas.append(str(fac.get(id=m).fecha_facturacion))
                else:
                    print("")
            else:
                print("")
        return fechas

    context={"title": "ElectRave user page",'use': use, 'datos': get_graph, 'fechas': get_graph1, 'user': usuario, 'usuario': usuari}
    return render(request,"paginaUsuarios.html",context
    )


def gestion_usuario(request):
    return render(request, 'listaUsuarios.html')

def inicioUsuario(request):
    user = User.objects.all()
    fac = Factura.objects.all()
    context={'use':user, 'fac': fac}
    return render(request, 'bienvenida.html', context)