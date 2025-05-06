from django.shortcuts import render, redirect
from usuarios.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from fichas.models import Ficha


def home(request):
    fichas = None
    if request.user.is_authenticated:
        fichas = Ficha.objects.filter(usuario=request.user)
    return render(request, 'home.html', {'fichas': fichas})


