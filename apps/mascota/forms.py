from django import forms

from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):

    class Meta:

        model = Mascota

        fields = [
            'nombre',
            'raza',
            'genero',
            'edad',
            'descripcion',
            'imagen',
        ]

        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'genero': 'Genero',
            'edad': 'Edad',
            'descripcion': 'Descripcion',
            'imagen': 'Imágen',
        }

        '''
        VER WIDGETS PARA ELIMINACION LOGICA (boton de estado)
        '''

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Ingrese el nombre de su mascota',
                'id': 'nombre'
            }),

            'raza':
                forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la raza de su mascota',
                    'id': 'raza'
                }),

            'genero':
                forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Masculino / Femenino',
                    'id': 'genero'
                }),

            'edad':
                forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la edad de su mascota',
                    'id': 'edad'
                }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese una breve descripcion',
                'id':'descripcion'
            }),

            'imagen': forms.FileInput(attrs={
                'class':'FileInput',
                'id': 'imagen'
            }),

        }
