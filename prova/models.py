from django.db import models
from perfil.models import Perfil
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Prova(models.Model):
    nome_prova = models.CharField(max_length=255, blank=True, null=True)
    perfil_autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nota = models.FloatField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    serie = models.CharField(max_length=10, blank=True, null=True)
    recuperacao = models.BooleanField(default=False)
    publico = models.BooleanField(default=False)
    teste_texto = RichTextField()
    slug = models.SlugField(default=None, blank=True, null=True)
    
    def __str__(self):
        return self.nome_prova
    
    def save(self):
        if not self.nome_prova:
            
            self.nome_prova = f'Prova {self.serie} {self.data_criacao}'

        if not self.slug:
            self.slug = slugify(f'{self.nome_prova}-{self.serie}')
            
            
        return super().save()
    
    