from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.serializers import serialize
from django.http import HttpResponse
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
import json
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
    print('Datos enviados : "%s"' % request.body)
    return HttpResponse("Ok")


def TraerTodasLasMascotasJSON(request):
    qs = serialize('python', Mascota.objects.all())
    resultado = []
    for d in qs:
        pk = d['pk']
        d['fields']['pk']=pk
        resultado.append(d['fields'])
    output = json.dumps(resultado)
    return HttpResponse(output, content_type="application/json")
