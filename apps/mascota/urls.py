from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import redirect_view, AgregarMascotaMovil

from apps.mascota.views import ListadoMascota, ActualizarMascota, CrearMascota, EliminarMascota, \
    TraerTodasLasMascotasJSON

urlpatterns = [
    path('redirect/', redirect_view),
    path('nuevo/', login_required(CrearMascota.as_view()), name='mascota_crear'),
    path('listar/', login_required(ListadoMascota.as_view()), name='mascota_listar'),
    path('json/', TraerTodasLasMascotasJSON, name='mascota_json'),
    # pk parametro para buscar (Primary Key generada por django automaticamente)
    path('editar/<int:pk>/', ActualizarMascota.as_view(), name='mascota_editar'),
    path('eliminar/<int:pk>/', EliminarMascota.as_view(), name='mascota_eliminar'),
    path('agregarmascotamovil/', AgregarMascotaMovil, name='mascota_agregar_movil')

]
