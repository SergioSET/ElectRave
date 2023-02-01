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
    path('login', authentication.views.login_page, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='home'), name='logout'),
    path('', blog.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('accountPage/<int:id_usuario>', blog.views.index , name='accountPage'),
    path('accountPageUsersAdmin/', authentication.views.listar_usuarios_admin, name='gestion_users_admin'),
    path('accountPageUsersGerente/', authentication.views.listar_usuarios_gerente, name='gestion_users_gerente'),
    path('accountPageUsersOperador/', authentication.views.listar_usuarios_operador, name='gestion_users_operador'),
    path('modificarUsuarios/<int:id_usuario>', authentication.views.modificar_usuario, name='modificar-usuarios'),
    path('actualizarUsuarios/<int:id_usuario>', authentication.views.actualizar_usuario, name='actualizar-usuarios'),
    path('eliminarUsuarios/<int:id_usuario>', authentication.views.eliminar_usuario, name='eliminar-usuarios'),
    path('agregarUser', authentication.views.signup_page, name='agregar-usuario'),
    path('gestionFacturas/<str:usuarioU>', authentication.views.listar_factura, name='gestion-factura'),
    path('gestionFacturasCliente/', authentication.views.listar_factura_cliente, name='gestion-factura-cliente'),
    path('procesoPago/<int:id_usuario>', authentication.views.pagos, name='gestion-pago'),
    path('procesoPagoCliente/<int:id_usuario>', authentication.views.pagosCliente, name='gestion-pago-cliente'),
    path('pagado/<int:id_usuario>', authentication.views.cambiarEstadoPago, name='factura-paga'),
    path('pagadoCliente/<int:id_usuario>', authentication.views.cambiarEstadoPagoCliente, name='factura-paga-cliente'),
    path('inicioUsuario', blog.views.inicioUsuario, name='inicio-usuario'),
    path('factura/<int:id_factura>', authentication.views.mostrarFactura, name='ver-factura'),
    path('crearFactura/', authentication.views.signup_Fac, name='crear-factura'),
    path('verInfo/<str:usuario>', authentication.views.ver_perfil, name='ver-usuario'),
]
