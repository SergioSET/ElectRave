from django.contrib.auth import login, authenticate, logout # add to imports
from django.shortcuts import render, redirect
from . import forms
from django.conf import settings

def home(request):
    return render(
        request,
        "home.html",
        {
            "title": "ElectRave page",
        },
    )

# def login(request):
 #   return render(
#        request,
 #       "login.html",
 #       {
#            "title": "ElectRave login page",
#        },
 #   )

#*def register(request):
#    return render(
#        request,
#        "register.html",
 #       {
#            "title": "ElectRave register page",
#        },
#    )

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "ElectRave user page",
        },
    )
def loginn(request):
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
                return redirect('index-usuario')
        message = 'Usuario o contraseña no validos'
    return render(request, 'login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'register.html', context={'form': form})

def index(request):
    return render(request, 'index.html')
    
def gestion_usuario(request):
    return render(request, 'gestion_usuarios.html')

def listar_usuarios(request):
    usuarios=Usuario.object.all()
    data={
        'usuarios':usuarios
    }
    return render(request,'gestion_usuarios.html',data)