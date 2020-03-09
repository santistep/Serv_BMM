from django.urls import path

from .views import redirect_view

from apps.mascota.views import index
from apps.mascota.views import mascota_view, mascota_list, mascota_edit, mascota_delete

urlpatterns = [
    path('redirect/', redirect_view),
    path('', index, name='index'),
    path('nuevo/', mascota_view, name='mascota_crear'),
    path('listar/', mascota_list, name='mascota_listar'),
    path('editar/<int:id_mascota>/', mascota_edit, name='mascota_editar'),
    path('eliminar/<int:id_mascota>/', mascota_delete, name='mascota_eliminar'),
]
