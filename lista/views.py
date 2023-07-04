from django.shortcuts import render, redirect
from lista.forms import ListaViagemForm
from lista.models import ListaViagem

def criar_lista(request):
    if request.method == 'POST':
        form = ListaViagemForm(request.POST)
        if form.is_valid():
            lista = form.save(commit=False)
            lista.usuario = request.user
            lista.save()
            return redirect('nome_da_rota')
    else:
        form = ListaViagemForm()
    return render(request, 'criar_lista.html', {'form': form})

def editar_lista(request, lista_id):
    lista = ListaViagem.objects.get(id=lista_id)
    if request.method == 'POST':
        form = ListaViagemForm(request.POST, instance=lista)
        if form.is_valid():
            form.save()
            return redirect('nome_da_rota')
    else:
        form = ListaViagemForm(instance=lista)
    return render(request, 'editar_lista.html', {'form': form, 'lista': lista})

def deletar_lista(request, lista_id):
    lista = ListaViagem.objects.get(id=lista_id)
    lista.delete()
    return redirect('nome_da_rota')
