"""desarrolloPrototipo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# from django.contrib.auth.views import login_required, logout_then_login

from django.urls import path, include
from django.conf import settings
from django.contrib.auth.decorators import login_required

from apps.usuario.views import Login, RegistroUsuario, Logout
#from apps.home.views import Inicio
from apps.mascota.views import ListadoMascota
from apps.perdido.views import ListadoPerdido

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascota/', include('apps.mascota.urls')),
    path('mascota/', login_required(ListadoMascota.as_view()), name='mascota_listar'),
    path('perdido/', include('apps.perdido.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('registrar/', RegistroUsuario.as_view(), name='registrar'),
    path('home/', ListadoPerdido.as_view(), name='index'),
    path('', ListadoPerdido.as_view(), name='perdido_listar'),

    # path('', login,{'template_name' = 'login.html'}, name= 'login'),

    path('accounts/login/', Login.as_view(), name='login'),
    path('logged_out/', Logout.as_view(), name='logged_out'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
