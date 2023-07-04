from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Crie um novo usuário
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        
        return HttpResponse('Registro realizado com sucesso!')
    else:
        return render(request, 'register.html')

