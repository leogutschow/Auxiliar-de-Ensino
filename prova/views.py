from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FormProva
# Create your views here.

class ProvaEdit(FormView, LoginRequiredMixin):
    template_name = 'prova/prova_edit.html'
    form_class = FormProva