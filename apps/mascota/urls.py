from django.urls import path

from .views import redirect_view

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit

urlpatterns = [
    path('redirect/', redirect_view),
    path('', index, name='index'),
    path('nuevo/', mascota_view, name='mascota_crear'),
    path('listar/', mascota_list, name='mascota_listar'),
    path('editar/<int:id_mascota>/', mascota_edit, name='mascota_editar'),
]
