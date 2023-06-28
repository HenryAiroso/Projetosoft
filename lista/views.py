from django.shortcuts import render, redirect
from lista.forms import ListaViagemForm

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
