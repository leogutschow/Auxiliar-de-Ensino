from django.shortcuts import redirect, render
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from perfil.models import Perfil
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pergunta, Prova
from .forms import FormProva, FormPergunta


# Create your views here.

class ProvaDetalhe(LoginRequiredMixin, DetailView):
    template_name = 'prova/prova_detalhe.html'
    model = Prova
    context_object_name = 'prova'
    extra_context = {
        'perfil': Perfil.objects.all()
    }
    redirect_field_name = 'perfil:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        prova = self.get_object()
        perfil = Perfil.objects.get(usuario_id=self.request.user.id)
        context['prova'] = prova
        context['perfil'] = perfil

        return context



class ProvaEdit(UpdateView, LoginRequiredMixin):
    template_name = 'prova/prova_edit.html'
    form_class = FormProva
    model = Prova
    extra_context = {
        'perguntas' : Pergunta.objects.all()
    }
    redirect_field_name = 'perfil:login'


    def form_valid(self, form):
        data = form.cleaned_data
        
        form.save()

        return redirect('prova:prova_detalhe', data['slug'])


class ProvaCriar(CreateView, LoginRequiredMixin):
    template_name = 'prova/prova_edit.html'
    form_class = FormProva
    redirect_field_name = 'perfil:login'


    def form_valid(self, form):
        data = form.cleaned_data

        perfil = Perfil.objects.get(
            usuario_id=self.request.user.id
            )

        prova = Prova.objects.create(
            nome_prova=data['nome_prova'],
            perfil_autor=perfil,
            nota=data['nota'],
            serie=data['serie'],
            recuperacao=data['recuperacao'],
            publico=data['publico'],
            teste_texto=data['teste_texto'],
            )
        
        prova.save()

        return redirect('prova:prova_detalhe', prova.slug)

class ProvaDeletar(DeleteView, LoginRequiredMixin):
    model = Prova
    template_name = 'prova/prova_delete.html'
    redirect_field_name = 'perfil:login'
    success_url = 'dashboard:index'
    context_object_name = 'prova'
    

    def delete(self, request, *args, **kwargs):

        prova = self.get_object

        prova = Prova.objects.get(id=prova.id)

        prova.delete()
        

        return redirect('dashboard:provas')

    