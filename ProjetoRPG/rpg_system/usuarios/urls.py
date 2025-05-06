from django.urls import path
from . import views

app_name = 'usuarios'  # Namespace para evitar conflitos com outros apps

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]
