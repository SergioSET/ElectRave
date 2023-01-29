from django.contrib.auth import login, authenticate, logout # add to imports
from django.shortcuts import render, redirect
from . import forms
from django.conf import settings
from authentication.models import User, Factura
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('accountPage')
        message = 'Usuario o contraseña no validos'
    return render(request, 'authentication\login.html', context={'form': form, 'message': message})

# C:\Users\juane\Desktop\Nueva carpeta\App\authentication\templates\authentication\login.html
def logout_user(request):
    logout(request)
    return redirect('home')


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

def agregarUser(request):
    form = forms.formularioAgregar()
    if request.method == 'POST':
        form = forms.formularioAgregar(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('listar-usuarios')
    use = User.objects.all()        
    context={'form': form, 'use': use}
    return render(request, 'agregarUsuarios.html', context)


def listar_usuarios(request):
    use = User.objects.all()
    context = {'use': use}
    return render(request,"listaUsuarios.html",context)



def listar_factura(request):
    use = User.objects.all()
    fac = Factura.objects.all()
    context = {'use': use, 'fac':fac}
    return render(request,"listaFacturas.html",context)


def geeks_view(request):
    # create a dictionary
    context = {
        "data" : "Hola ",
    }
    # return response
    return render(request, "listaUsuarios.html", context)


def modificar_usuario(requets,id_alumno):
    usuario = User.objects.filter(id=id_alumno).first()
    form = forms.formularioAlumno(instance=usuario)
    use = User.objects.all()
    return render(requets,"modificarUsuarios.html",{"form":form,'usuario':usuario,'use':use})


def actualizar_usuario(request,id_alumno):
    usuario= User.objects.get(pk=id_alumno)
    form = forms.formularioAlumno(request.POST,instance=usuario)
    if form.is_valid():
        form.save()
    usuarios = User.objects.all()
    context = {'use': usuarios}
    return render(request,"listaUsuarios.html",context)

def eliminar_usuario(request, id_alumno):
    usuario= User.objects.get(pk=id_alumno)
    usuario.delete()
    usuarios = User.objects.all()
    return render(request,"listaUsuarios.html",{"use":usuarios,"mensaje":'Ok'})

def pagos(request,id_alumno):
    id = id_alumno
    return render(request, 'formularioPago.html', {"id":id})

def cambiarEstadoPago(request, id_alumno):
    pago= Factura.objects.get(pk=id_alumno)
    pago.Pagado = 'true'
    pago.save()
    facturas = Factura.objects.all()
    use = User.objects.all()
    return render(request,"listaFacturas.html",{"fac":facturas,"mensaje":'Ok', "use":use})
