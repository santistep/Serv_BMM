import json
from uuid import uuid4

from django.contrib.auth.views import LogoutView, auth_logout
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
import base64

from apps.usuario.forms import RegistroForm, FormularioLogin
from apps.usuario.models import Usuario


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('mascota_listar')


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('perdido_listar')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


class Logout(LogoutView):
    next_page = reverse_lazy('perdido_listar')
    template_name = 'logged_out.html'
    extra_context = None

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        auth_logout(request)
        next_page = self.get_next_page()
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)




def LoginMovil(request):
    datos = json.loads(request.body)
    email = datos['email']
    contrasena = datos['contrasena']
    if Usuario.objects.filter(email=email).exists():
        usuario_existente = Usuario.objects.get(email=email)
        if usuario_existente.contrasena == contrasena:
            respuesta = '0'
        else:
            respuesta = '2'
    else:
        respuesta = '1'
    return HttpResponse(respuesta)


def RegistroUsuarioMovil(request):
    datos = json.loads(request.body)
    if Usuario.objects.filter(email=datos['email']).exists():
        respuesta = "1"
    else:
        usuario = Usuario()
        usuario.nombre_usuario = datos['nombre_usuario']
        usuario.email = datos['email']
        usuario.contrasena = datos['contrasena']
        usuario.telefono = datos['telefono']
        usuario.save()
        respuesta = '0'
    return HttpResponse(respuesta)
