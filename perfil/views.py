
from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import FormView

from amigos.models import ListaAmigos
from .models import Perfil
from .forms import FormUsuario
from prova.models import Prova
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class SignIn(FormView):
    template_name = 'perfil/signin.html'
    form_class = FormUsuario
    
    def form_valid(self, form):
        cadastro_usuario = form.cleaned_data
        
        user = User.objects.create_user(
            username=cadastro_usuario['username'], 
            email=cadastro_usuario['email'], 
            password=cadastro_usuario['password'],
            first_name=cadastro_usuario['first_name'], 
            last_name=cadastro_usuario['last_name']
        )
        
        user.save()
        
        perfil = Perfil.objects.create(
            usuario=user,
            email=cadastro_usuario['email'], 
            nome=cadastro_usuario['first_name'], 
            sobrenome=cadastro_usuario['last_name']
        )
        
        perfil.save()
        
        return redirect('perfil:login')
    
class LogIn(LoginView):
    template_name = 'perfil/login.html'
    next_page = 'dashboard:index'
    
class LogOut(LogoutView):
    pass

class PerfilUsuario(DetailView):
    template_name = 'perfil/perfil_index.html'
    model = Perfil
    context_object_name = 'perfil'


    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        perfil = self.get_object()
        lista_amigos = ListaAmigos.objects.get(user=perfil.usuario_id)
        contexto['perfil'] = perfil
        contexto['lista_amigos'] = lista_amigos
        

        return contexto

  
    