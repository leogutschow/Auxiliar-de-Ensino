
from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Pergunta, Prova

class FormProva(ModelForm):

    class Meta:
        model = Prova
        fields = (
            'nome_prova', 'nota', 'serie', 'recuperacao', 'publico',
            'slug',
            )
        widgets = {
            'slug': forms.HiddenInput()
        }


class FormPergunta(ModelForm):
    model = Pergunta
