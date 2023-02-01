from django.contrib.auth import login, authenticate, logout # add to imports
from django.shortcuts import render, redirect
from . import forms
from django.conf import settings
from authentication.models import User, Factura
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.http import FileResponse
from django.template.loader import get_template
from io import BytesIO
from reportlab.pdfgen import canvas



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
                return redirect('inicio-usuario')
        message = 'Usuario o contraseña no validos'
    return render(request, 'authentication\signin.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('home')


def signup_page(request):
    use= User.objects.all()
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('gestion_users_admin')
    return render(request, 'authentication/signup.html', context={'form': form, 'use':use})

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

def agregarFac(request):
    form = forms.BandForm()
    if request.method == 'POST':
        form = forms.BandForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('gestion_users_admin')
    use = User.objects.all()        
    context={'form': form, 'use': use}
    return render(request, 'crearFactura.html', context)

def signup_Fac(request):
    use= User.objects.all()
    form = forms.BandForm()
    if request.method == 'POST':
        form = forms.BandForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('gestion_users_admin')
    return render(request, 'authentication/signup_fac.html', context={'form': form, 'use':use})


def listar_usuarios_admin(request):
    use = User.objects.all()
    context = {'use': use}
    return render(request,"listaUsuariosAdmin.html",context)

def listar_usuarios_operador(request):
    use = User.objects.all()
    fac = Factura.objects.all()
    context = {'use': use, 'fac':fac}
    return render(request,"listaUsuariosoperador.html",context)

def listar_usuarios_gerente(request):
    use = User.objects.all()
    context = {'use': use}
    return render(request,"listaUsuariosgerentes.html",context)


def listar_factura(request,usuarioU):
    use = User.objects.all()
    usuario = use.get(username=usuarioU)
    fac = Factura.objects.all()
    context = {'use': use, 'fac':fac, 'usuario': usuario}
    return render(request,"listaFacturas.html",context)

def listar_factura_cliente(request):
    use = User.objects.all()
    fac = Factura.objects.all()
    context = {'use': use, 'fac':fac}
    return render(request,"listaFacturascliente.html",context)

def modificar_usuario(requets,id_usuario):
    usuario = User.objects.filter(id=id_usuario).first()
    form = forms.formularioAlumno(instance=usuario)
    use = User.objects.all()
    return render(requets,"modificarUsuarios.html",{"form":form,'usuario':usuario,'use':use})


def actualizar_usuario(request,id_usuario):
    usuario= User.objects.get(pk=id_usuario)
    rol = usuario.role
    form = forms.formularioAlumno(request.POST,instance=usuario)
    if form.is_valid():
        form.save()
    usuarios = User.objects.all()
    context = {'use': usuarios}

    if rol == 'ADMIN':
        return render(request,"listaUsuariosAdmin.html",context)
    else:
        return render(request,"listaUsuariosoperador.html",context)

def eliminar_usuario(request, id_usuario):
    usuario= User.objects.get(pk=id_usuario)
    usuario.delete()
    usuarios = User.objects.all()
    return render(request,"listaUsuarios.html",{"use":usuarios,"mensaje":'Ok'})

def pagos(request,id_usuario):
    id = id_usuario
    return render(request, 'formularioPago.html', {"id":id})

def pagosCliente(request,id_usuario):
    id = id_usuario
    return render(request, 'formularioPagoCliente.html', {"id":id})

def cambiarEstadoPago(request, id_usuario):
    pago= Factura.objects.get(pk=id_usuario)
    pago.Pagado = 'true'
    pago.save()
    facturas = Factura.objects.all()
    use = User.objects.all()
    usuario = use.get(username=pago.cliente)
    return render(request,"listaFacturas.html",{"fac":facturas,"mensaje":'Ok', "use":use, "usuario":usuario})

def cambiarEstadoPagoCliente(request, id_usuario):
    pago= Factura.objects.get(pk=id_usuario)
    pago.Pagado = 'true'
    pago.save()
    facturas = Factura.objects.all()
    use = User.objects.all()
    return render(request,"listaFacturascliente.html",{"fac":facturas,"mensaje":'Ok', "use":use})

def mostrarFactura(request, id_factura):
    use = User.objects.all()
    fac = Factura.objects.all()
    clienteh = fac.get(id=id_factura).cliente
    usuario = use.get(username=clienteh)
    factura = fac.get(id=id_factura)
    context = {'Usuario': usuario, 'Factura': factura}
    return render(request,"factura.html",context)


def ver_perfil(request, usuario):
    user = User.objects.get(username=usuario)
    use = User.objects.all()
    context = {'user': user, 'use': use}
    return render(request,"verInfo.html",context)
