from django.db import models
from django.contrib.auth import get_user_model
from fichas.models import Ficha


class FichaCombate(models.Model):
    usuario = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='fichas_combate'
    )
    ficha_base = models.OneToOneField(
        'fichas.Ficha',
        on_delete=models.CASCADE,
        related_name='combate',
        null=True,   # Permite nulos para facilitar a migração
        blank=True
    )
    vida = models.IntegerField(default=100)
    mana = models.IntegerField(default=50)
    atributos = models.JSONField(default=dict)
    barras_personalizaveis = models.JSONField(default=dict)
    dados = models.JSONField(default=dict)
    anotacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"FichaCombate: {self.ficha_base} - Usuário: {self.usuario}"


