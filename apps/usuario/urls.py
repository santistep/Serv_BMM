from django.urls import path
from apps.usuario.views import index_usuario

urlpatterns = [
    path('', index_usuario),
]
