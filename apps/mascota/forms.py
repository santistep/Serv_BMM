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
            'usuario',
        ]
        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'genero': 'Genero',
            'edad': 'Edad',
            'descripcion': 'Descripcion',
            'usuario': 'Usuario',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
