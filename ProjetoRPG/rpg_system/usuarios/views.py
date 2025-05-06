from django.shortcuts import render, redirect
from .forms import PerfilForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def registro_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona se o usuário já estiver logado
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona se já está logado
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


@login_required
def perfil_usuario(request):
    form = PerfilForm(instance=request.user)  # Carrega os dados do usuário
    if request.method == 'POST':  # Permite edição no mesmo template
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  # Salva os dados editados
            return redirect('usuarios:perfil_usuario')
    return render(request, 'usuarios/perfil_usuario.html', {'form': form, 'usuario': request.user})
