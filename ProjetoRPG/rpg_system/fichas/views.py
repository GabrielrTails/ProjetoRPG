from django.shortcuts import render, redirect
from .forms import FichaForm
from django.http import HttpResponse
from .models import Ficha
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import logging
logger = logging.getLogger(__name__)
##############################################


@login_required
def lista_fichas(request):
    fichas = Ficha.objects.select_related('ficha_combate').filter(usuario=request.user)
    return render(request, 'fichas/lista_fichas.html', {'fichas': fichas})


@login_required
def criar_ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.usuario = request.user
            ficha.save()
            messages.success(request, 'Ficha criada com sucesso!')
            return redirect('lista_fichas')
        else:
            messages.error(request, 'Houve um erro ao criar a ficha. Verifique os dados.')
    else:
        form = FichaForm()
    return render(request, 'fichas/criar_ficha.html', {'form': form})


@login_required
def editar_ficha(request, ficha_id):
    ficha = get_object_or_404(Ficha, id=ficha_id, usuario=request.user)
    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return redirect('lista_fichas')
    else:
        form = FichaForm(instance=ficha)
    return render(request, 'fichas/editar_ficha.html', {'form': form, 'ficha': ficha})



@login_required
def deletar_ficha(request, ficha_id):
    ficha = get_object_or_404(Ficha, id=ficha_id, usuario=request.user)
    if request.method == 'POST':
        ficha.delete()
        messages.success(request, 'Ficha deletada com sucesso!')
        return redirect('lista_fichas')
    return render(request, 'fichas/deletar_ficha.html', {'ficha': ficha})