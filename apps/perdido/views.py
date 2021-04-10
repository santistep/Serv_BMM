from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.perdido.forms import PerdidoForm
from apps.perdido.models import Perdido


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response


class CrearPerdido(CreateView):
    model = Perdido
    form_class = PerdidoForm
    template_name = 'perdido/perdido_form.html'
    success_url = reverse_lazy('perdido_listar')


class ListadoPerdido(ListView):
    model = Perdido
    template_name = 'perdido/perdido_list.html'
    context_object_name = 'perdidos'


class ActualizarPerdido(UpdateView):
    model = Perdido
    form_class = PerdidoForm
    template_name = 'perdido/perdido_form.html'
    success_url = reverse_lazy('perdido_listar')


class EliminarPerdido(DeleteView):
    model = Perdido
    success_url = reverse_lazy(
        'perdido_listar')  # ELIMINACION LOGICA -Debo sacar este reverse_lazy para redefinir el estado-


'''
ELIMINACION LOGICA

Redefino el metodo post para cambiar el estado y no eliminar todo de la base de datos

    def post(self, request, pk, *args, **kwargs):
        object = Mascota.object.get(id = pk)
        object.estado = False
        object.save()
        return redirect('mascota_listar')
'''
