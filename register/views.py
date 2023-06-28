from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecionar para a página inicial após o registro
    else:
        form = UserCreationForm()
    
    return render(request, 'register/register.html', {'form': form})

