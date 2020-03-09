from django import forms

from apps.perdido.models import Perdido


class PerdidoForm(forms.ModelForm):

    class Meta:

        model = Perdido

        fields = [
            'raza',
            'genero',
            'descripcion',
            'fecha_denuncia',
            'usuario',
        ]
        labels = {
            'raza': 'Raza',
            'genero': 'Genero',
            'descripcion': 'Descripcion',
            'fecha_denuncia': "Fecha",
            'usuario': 'Usuario',
        }
        widgets = {
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_denuncia': forms.DateInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
