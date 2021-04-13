import base64
import json
from uuid import uuid4

from django.core.files.base import ContentFile
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

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
    datos = json.loads(request.body)
    mascota = Mascota()
    mascota.nombre = datos['nombre']
    mascota.especie = datos['especie']
    mascota.raza = datos['raza']
    mascota.color = datos['color']
    mascota.edad = datos['edad']
    mascota.genero = datos['genero']
    mascota.tamano = datos['tamano']
    mascota.recompensa = datos['recompensa']
    mascota.descripcion = datos['descripcion']
    mascota.usuario = datos['usuario']
    mascota.imagen = base64_to_image(datos['imagen'])
    mascota.ultima_posicion_conocida = datos['ultima_posicion_conocida']
    mascota.save()
    return HttpResponse("Ok")


def image_to_base64(image):
    with open(image, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return image_data


def base64_to_image(base64_string):
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=uuid4().hex + "." + ext)


def TraerTodasLasMascotasJSON(request):
    diccionario_de_mascotas = serialize('python', Mascota.objects.all())

    resultado = []
    for mascota in diccionario_de_mascotas:

        primary_key = mascota['pk']
        mascota['fields']['pk'] = primary_key

        ruta_de_imagen = mascota['fields']['imagen']
        imagen_base64 = image_to_base64(ruta_de_imagen)
        mascota['fields']['imagen'] = imagen_base64

        resultado.append(mascota['fields'])

    output = json.dumps(resultado)
    return HttpResponse(output, content_type="application/json")
