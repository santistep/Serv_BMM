import json
import smtplib
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

from pytz import unicode

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
    email = datos['inputEmail']
    contrasena = datos['inputPassword']
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
    peticion = request.body
    peticion = unicode(peticion, 'iso-8859-1')
    datos = json.loads(peticion)

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

def RecoverPasswordMovil(request):
    #Leo datos json
    datos = json.loads(request.body)

    #Obtengo dato que quiero
    email = datos['inputEmailRecover']

    #Chequeo que el usuario este registrado, if True, envio la contraseña por email

    if Usuario.objects.filter(email=email).exists():
        usuario_existente = Usuario.objects.get(email=email)
        usuario_password = usuario_existente.contrasena

        #Variables que almacenan el mensaje y el asunto
        message = f"Hola, esta es tu contraseña {usuario_password}. Te recomendamos cambiarla al reingresar"
        subject = "Recuperacion Contraseña Footprints"

        message = 'Subject: {}\n\n{}'.format(subject,message)

        # Creo un objeto smtp desde la libreria (servidor de correo, puerto a utilizar)
        server = smtplib.SMTP('smtp.gmail.com', 25)
        # Defino el uso del protocolo tls
        server.starttls()
        # Autentico con mi cuenta de correo (cuenta, password)
        server.login('footprintsbmm@gmail.com', 'footprints1234')
        # Envio mail (email desde el cual se envia, email destinatario, mensaje)
        server.send("footprintsbmm@gmail.com", email, message)

        # Salgo de la cuenta
        server.quit()

        respuesta = '0'

    else:
        respuesta = '1'

    return HttpResponse(respuesta)



