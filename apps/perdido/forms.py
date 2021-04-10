from django import forms

from apps.perdido.models import Perdido


class PerdidoForm(forms.ModelForm):

    class Meta:

        model = Perdido

        fields = [
            'fecha_denuncia',
            'descripcion',
            'mascota',
            'ciudad',
            'barrio',
            'contacto',
            'imagen'

        ]
        labels = {
            'fecha_denuncia': "Fecha",
            'descripcion': 'Descripcion',
            'mascota': 'Mascota',
            'ciudad': 'Ciudad',
            'barrio': 'Barrio',
            'contacto': 'contacto',
            'imagen': 'Imágen'

        }
        widgets = {
            'fecha_denuncia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fecha actual',# Ver como es el manejo de fecha
                'id': 'fecha_denuncia'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describa brevemente donde y como se perdio',
                'id': 'descripcion'
            }),

            'mascota': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Elija la mascota de la lista',# No funciona en vista desplegable?
                'id': 'mascota'
            }),

            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la ciudad',
                'id': 'ciudad'
            }),

            'barrio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el barrio',
                'id': 'barrio'
            }),

            'contacto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese un medio de contacto',
                'id': 'contacto'

            }),

        }
