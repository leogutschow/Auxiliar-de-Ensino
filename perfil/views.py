from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import FormView
from .models import Perfil
from .forms import FormUsuario
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Dashboard(ListView):
    template_name = 'perfil/dashboard.html'
    model = Perfil
    context_object_name = 'perfil'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
            
        return super().dispatch(request, *args, **kwargs)


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
        
        return redirect('dashboard')
    
class LogIn(LoginView):
    template_name = 'perfil/login.html'
    next_page = 'dashboard'
    
class LogOut(LogoutView):
    pass

    
    
    