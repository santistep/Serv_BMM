from django import forms

from apps.perdido.models import Perdido


class PerdidoForm(forms.ModelForm):

    class Meta:

        model = Perdido

        fields = [
            'fecha_denuncia',
            'mascota',
            'ultima_posicion_conocida',
            'imagen'

        ]
        labels = {
            'fecha_denuncia': "Fecha",
            'mascota': 'Mascota',
            'ultima_posicion_conocida': 'Ultima direccion en donde se vio a la mascota',
            'imagen': 'Imágen'

        }
        widgets = {
            'fecha_denuncia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fecha actual',# Ver como es el manejo de fecha
                'id': 'fecha_denuncia'
            }),

            'mascota': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Elija la mascota de la lista',# No funciona en vista desplegable?
                'id': 'mascota'
            }),

            'ultima_posicion_conocida': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la ultima direccion en la que vio a su mascota',
                'id': 'ciudad'
            })



        }
