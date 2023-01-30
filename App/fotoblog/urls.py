"""fotoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
import blog.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('home/', blog.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('accountPage/', blog.views.index , name='accountPage'),
    path('accountPageUsers/', authentication.views.listar_usuarios, name='gestion_users'),
    path('listaUsuarios/', authentication.views.listar_usuarios, name='listar-usuarios'),
    path('modificarUsuarios/<int:id_alumno>', authentication.views.modificar_usuario, name='modificar-usuarios'),
    path('actualizarUsuarios/<int:id_alumno>', authentication.views.actualizar_usuario, name='actualizar-usuarios'),
    path('eliminarUsuarios/<int:id_alumno>', authentication.views.eliminar_usuario, name='eliminar-usuarios'),
    path('agregarUser', authentication.views.agregarUser, name='agregar-usuario'),
    path('gestionFacturas/', authentication.views.listar_factura, name='gestion-factura'),
    path('procesoPago/<int:id_alumno>', authentication.views.pagos, name='gestion-pago'),
    path('pagado/<int:id_alumno>', authentication.views.cambiarEstadoPago, name='factura-paga'),
]
