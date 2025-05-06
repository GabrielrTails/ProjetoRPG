from django import forms
from .models import FichaCombate

class FichaCombateForm(forms.ModelForm):
    class Meta:
        model = FichaCombate
        fields = ['vida', 'mana', 'atributos', 'barras_personalizaveis', 'anotacoes']
        widgets = {
            'vida': forms.NumberInput(attrs={'class': 'form-control'}),
            'mana': forms.NumberInput(attrs={'class': 'form-control'}),
            'atributos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'barras_personalizaveis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'anotacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
