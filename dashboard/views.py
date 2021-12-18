from django.shortcuts import render, redirect
from django.views.generic import ListView
from perfil.models import Perfil
from prova.models import Prova


# Create your views here.

class Index(ListView):
    template_name = 'dashboard/dashboard.html'
    model = Perfil
    context_object_name = 'perfil'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('perfil:login')
            
        return super().dispatch(request, *args, **kwargs)
    

class Provas(Index):
    extra_context = {
        'provas' : Prova.objects.all()
    }
    context_object_name = 'provas'
    
    def get_queryset(self):
        query_set = Prova.objects.filter(perfil_autor_id=self.request.user.id)
        return query_set