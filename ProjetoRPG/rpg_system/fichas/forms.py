from django import forms
from .models import Ficha
from django.core.exceptions import ValidationError
import json



class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['sistema', 'nome_personagem', 'raça', 'classe', 'nível', 'atributos']
        widgets = {
            'sistema': forms.Select(attrs={'class': 'form-select'}),
            'nome_personagem': forms.TextInput(attrs={'class': 'form-control'}),
            'raça': forms.TextInput(attrs={'class': 'form-control'}),
            'classe': forms.TextInput(attrs={'class': 'form-control'}),
            'nível': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'atributos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

def clean_atributos(self):
        data = self.cleaned_data['atributos']
        try:
            json.loads(data)  # Tenta carregar os atributos como JSON
        except json.JSONDecodeError:
            raise ValidationError('Por favor, insira um JSON válido.')
        return data