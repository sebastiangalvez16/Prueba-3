from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente_id', 'edad', 'genero', 'saldo', 'active', 'nivel_de_satisfaccion']
        widgets = {
            'cliente_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del Cliente'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Saldo'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nivel_de_satisfaccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nivel de Satisfacción'}),
        }
        labels = {
            'cliente_id': 'ID del Cliente',
            'edad': 'Edad',
            'genero': 'Género',
            'saldo': 'Saldo',
            'active': 'Activo',
            'nivel_de_satisfacción': 'Nivel de Satisfacción',
        }
