from django import forms
from lista.models import ListaViagem

class ListaViagemForm(forms.ModelForm):
    class Meta:
        model = ListaViagem
        fields = ['tema', 'descricao']