from django.forms import ModelForm
from .models import Prova

class FormProva(ModelForm):

    def clean(self):
        data = self.cleaned_data
        

    class Meta:
        model = Prova
        fields = (
            'nome_prova', 'nota', 'serie', 'recuperacao', 'publico',
            'teste_texto',  
            )