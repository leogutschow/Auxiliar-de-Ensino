
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import FormView
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

    
    
    