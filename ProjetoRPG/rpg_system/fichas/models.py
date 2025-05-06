from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

##########################
    
class Ficha(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Suporte ao modelo de usuário personalizado
    sistema = models.CharField(max_length=100, choices=[
        ('D&D 5e', 'Dungeons & Dragons 5ª Edição'),
        ('Vampiro', 'Vampiro: A Máscara'),
        ('Cthulhu', 'Chamado de Cthulhu')
    ])  # Opções de sistemas
    nome_personagem = models.CharField(max_length=100)
    raça = models.CharField(max_length=50, blank=True, null=True)
    classe = models.CharField(max_length=50, blank=True, null=True)
    nível = models.IntegerField(default=1)  # Nível inicial padrão
    atributos = models.JSONField()  # Dados flexíveis para atributos
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)  # Data de última modificação
    ficha_combate = models.OneToOneField(
        'combate.FichaCombate',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='base',  # Nome do reverse accessor ajustado
    )

    def __str__(self):
        return f'{self.nome_personagem} ({self.sistema}) - Nível {self.nível}'