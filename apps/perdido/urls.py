from django.urls import path

from .views import redirect_view

from apps.perdido.views import index
from apps.perdido.views import perdido_view, perdido_list, perdido_edit, perdido_delete

urlpatterns = [
    path('redirect/', redirect_view),
    path('', index, name='index'),
    path('nuevo/', perdido_view, name='perdido_crear'),
    path('listar/', perdido_list, name='perdido_listar'),
    path('editar/<int:id_perdido>/', perdido_edit, name='perdido_editar'),
    path('eliminar/<int:id_perdido>/', perdido_delete, name='perdido_eliminar'),
]
