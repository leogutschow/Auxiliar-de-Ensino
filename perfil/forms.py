from django import forms
from . models import Perfil
from django.contrib.auth.models import User


class FormUsuario(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Usuário'
        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['password'].label = 'Senha'
        self.fields['email'].label = 'E-Mail'
        
    def clean(self):
        data = self.cleaned_data
        usuario = data.get('username')
        nome = data.get('first_name')
        sobrenome = data.get('last_name')
        senha = data.get('password')
        email = data.get('email')
        
        if not email:
            self.add_error(
                'email',
                'Você precisa cadastrar um email'
            )
 
        
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(attrs={
                'id': 'senha_cadastro'
            })
        }
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        

        