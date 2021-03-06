from django.db.models import fields
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from perfil.models import Perfil
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pergunta, Prova, Resposta
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
    redirect_field_name = 'perfil:login'
    form_class = FormProva
    formset_pergunta = inlineformset_factory(Prova, Pergunta, 
                                    fields=('pergunta_texto',),
                                    form=FormProva)
    formset_respostas = inlineformset_factory(Pergunta, Resposta,
                                                fields=(
                                                    'resposta1',
                                                    'resposta2',
                                                    'resposta3',
                                                    'resposta4',
                                                    'resposta5',
                                                    'resposta6',
                                                    'resposta7',
                                                    'resposta8',
                                                    ),
                                                    form=FormPergunta)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['perguntas'] = self.formset_pergunta(self.request.post)
            data['respostas'] = self.formset_respostas(self.request.post)
        else:
            data['perguntas'] = self.formset_pergunta()
            data['respostas'] = self.formset_respostas()

        return data


    def form_valid(self, form):
        data = form.cleaned_data
        print(data)

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
    success_url = reverse_lazy('dashboard:provas')
    context_object_name = 'prova'
    

    def delete(self, request, *args, **kwargs):

        prova = self.get_object

        prova = Prova.objects.get(id=prova.id)

        prova.delete()
        

        return super().delete(self, request, *args, **kwargs)

    