from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import redirect_view

from apps.home.views import index
from apps.perdido.views import CrearPerdido, ListadoPerdido, ActualizarPerdido, EliminarPerdido

urlpatterns = [
    path('redirect/', redirect_view),
    path('', index, name='index'),
    path('nuevo/', login_required(CrearPerdido.as_view()), name='perdido_crear'),
    path('listar/', ListadoPerdido.as_view(), name='perdido_listar'),
    path('editar/<int:pk>/', login_required(ActualizarPerdido.as_view()), name='perdido_editar'),
    path('eliminar/<int:pk>/', login_required(EliminarPerdido.as_view()), name='perdido_eliminar'),
]
