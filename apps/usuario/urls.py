from django.urls import path

from apps.usuario.views import RegistroUsuario, LoginMovil, RegistroUsuarioMovil
from apps.usuario.views import Login, Logout

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('login', Login.as_view(), name="login"),
    path('logged_out', Logout.as_view(), name="logged_out"),
    path('loginmovil', LoginMovil, name="login_movil"),
    path('registrousuariomovil', RegistroUsuarioMovil, name="registro_usuario_movil")

]
