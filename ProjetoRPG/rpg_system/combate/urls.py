from django.urls import path
from .views import editar_ficha_combate, visualizar_ficha_combate

urlpatterns = [
    path('editar/<int:ficha_combate_id>/', editar_ficha_combate, name='editar_ficha_combate'),
    path('visualizar/<int:ficha_combate_id>/', visualizar_ficha_combate, name='visualizar_ficha_combate'),  # Caso precise visualizar
]

