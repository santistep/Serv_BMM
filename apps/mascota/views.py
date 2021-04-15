import base64
from uuid import uuid4

from django.core.files.base import ContentFile
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from pytz import unicode

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
from apps.perdido.models import Perdido
from apps.usuario.models import Usuario

'''
View recorre el siguiente ciclo:

1- dispatch(): valida la 'request=peticion' y elige que metodo se utilizo para eso
2- http_metod_not_allowed(): retorna error cuando se utilizo un metodo http no soportado o definido
3- options(): podemos definir mas metodos http

'''


class CrearMascota(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota_listar')


'''
PROTECCION A LA VISTA 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(self.template_name)
        else:
            return redirect('login')
'''
import json


class ListadoMascota(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'
    context_object_name = 'mascotas'
    # queryset =

    '''
    PROTECCION A LA VISTA 
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(self.template_name)
        else:
            return redirect('login')
'''


class ActualizarMascota(UpdateView):
    model = Mascota
    template_name = 'mascota/mascota_form.html'
    form_class = MascotaForm
    success_url = reverse_lazy('mascota_listar')


class EliminarMascota(DeleteView):
    model = Mascota
    success_url = reverse_lazy(
        'mascota_listar')  # ELIMINACION LOGICA -Debo sacar este reverse_lazy para redefinir el estado-


'''
ELIMINACION LOGICA

Redefino el metodo post para cambiar el estado y no eliminar todo de la base de datos

    def post(self, request, pk, *args, **kwargs):
        object = Mascota.object.get(id = pk)
        object.estado = False
        object.save()
        return redirect('mascota_listar')
'''


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response


# views.py

def AgregarMascotaMovil(request):
    peticion = request.body
    peticion = unicode(peticion, 'iso-8859-1')
    datos = json.loads(peticion)
    mascota = Mascota()
    perdido = Perdido()
    mascota.nombre = datos['nombre']
    mascota.especie = datos['especie']
    mascota.raza = datos['raza']
    mascota.color = datos['color']
    mascota.edad = datos['edad']
    mascota.genero = datos['genero']
    mascota.tamano = datos['tamano']
    mascota.descripcion = datos['descripcion']
    usuario = Usuario.objects.get(email=datos['usuario'])
    mascota.usuario = usuario
    mascota.imagen = base64_to_image(datos['imagen'])
    mascota.save()
    mascota.refresh_from_db()
    perdido.mascota = mascota
    perdido.ultima_posicion_conocida = datos['ultima_posicion_conocida']
    perdido.recompensa = datos['recompensa']
    perdido.fecha_denuncia = datos['fecha_y_hora']
    perdido.save()
    Respuesta = "Todo bien"
    return HttpResponse(Respuesta)


def image_to_base64(route):
    with open("media/"+route, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return image_data


def base64_to_image(base64_string):
    return ContentFile(base64.b64decode(base64_string), name=uuid4().hex + "." + "jpg")


from django.forms.models import model_to_dict


def TraerTodasLasMascotasJSON(request):
    querysetperdido = Perdido.objects.all()
    diccionario_de_perdido = serialize('python', querysetperdido)
    resultado = []

    for perdido in diccionario_de_perdido:
        primary_key = perdido['pk']
        perdido['fields']['pk'] = primary_key
        mascota = Mascota.objects.get(id=perdido['fields']['mascota'])
        perdido['fields'].pop('mascota', None)
        values = model_to_dict(mascota)
        imagen = image_to_base64(str(mascota.imagen))
        values.pop('id', None)
        values['imagen'] = imagen
        perdido['fields'].update(values)
        resultado.append(perdido['fields'])

    output = json.dumps(resultado, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    return HttpResponse(output, content_type="application/json")
