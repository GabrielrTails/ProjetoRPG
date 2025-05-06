from django.shortcuts import render, redirect, get_object_or_404
from .forms import FichaCombateForm
from fichas.models import Ficha
from .models import FichaCombate
from django.contrib.auth.decorators import login_required


@login_required
def editar_ficha_combate(request, ficha_combate_id):
    ficha_combate = get_object_or_404(FichaCombate, id=ficha_combate_id, usuario=request.user)
    if request.method == 'POST':
        form = FichaCombateForm(request.POST, instance=ficha_combate)
        if form.is_valid():
            form.save()
            return redirect('visualizar_ficha_combate', ficha_combate.id)
    else:
        form = FichaCombateForm(instance=ficha_combate)
    return render(request, 'combate/editar_ficha_combate.html', {'form': form, 'ficha_combate': ficha_combate})


def visualizar_ficha_combate(request, ficha_combate_id):
    ficha_combate = get_object_or_404(FichaCombate, id=ficha_combate_id)
    return render(request, 'combate/visualizar_ficha_combate.html', {'ficha_combate': ficha_combate})