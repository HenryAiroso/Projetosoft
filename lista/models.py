from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ListaViagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.tema