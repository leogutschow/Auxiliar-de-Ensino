from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from perfil.models import Perfil
from prova.models import Prova
from django.db.models import Q

#TODO Criar SideBar da Dashboard


# Create your views here.

class Index(LoginRequiredMixin, ListView):
    template_name = 'dashboard/dashboard.html'
    model = Perfil
    context_object_name = 'perfil'
    redirect_field_name = 'perfil:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil = Perfil.objects.get(usuario_id=self.request.user.id)
        provas = Prova.objects.filter(perfil_autor_id=perfil.id)
        print(perfil)
        context["perfil"] = perfil
        context["provas"] = provas
        return context
    

class Provas(Index):
    extra_context = {
        'provas': Prova.objects.all()
    }
    
    def get_queryset(self):
        query_set = Prova.objects.filter(perfil_autor_id=self.request.user.id)
        return query_set

