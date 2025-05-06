from django.urls import path
from .views import lista_fichas, criar_ficha, editar_ficha, deletar_ficha

urlpatterns = [
    path('', lista_fichas, name='lista_fichas'),
    path('criar/', criar_ficha, name='criar_ficha'),
    path('<int:ficha_id>/editar/', editar_ficha, name='editar_ficha'),
    path('<int:ficha_id>/deletar/', deletar_ficha, name='deletar_ficha'),
]