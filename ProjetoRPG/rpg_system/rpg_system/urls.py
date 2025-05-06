from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include  # Importa a view de registro do app fichas
from .views import home # Importa as views da página inicial e do perfil do usuário
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# View simples para o caminho vazio (home)
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    # Rota para administração do Django
    path('admin/', admin.site.urls, name='admin'),

    path('', home, name='home'),
    path('fichas/', include('fichas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('combate/', include('combate.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)