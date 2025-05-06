from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'foto_perfil', 'password1', 'password2']  # Campos válidos

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['foto_perfil']  # Apenas o campo de imagem
        widgets = {
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }