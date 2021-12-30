from django.db import models
from django.contrib.auth.models import User
from especializacao.models import Especializacao
from django.utils import timezone

# Create your models here.

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    especializacao = models.ForeignKey(Especializacao, on_delete=models.DO_NOTHING, default=2)
    data_criacao = models.DateTimeField(default=timezone.now)
    foto_perfil = models.ImageField(upload_to='perfil/%Y/%m', blank=True, null=True)
    slug = models.SlugField(default=None)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}' or self.usuario
    
    def save(self):
        if not self.slug:
            self.slug=self.usuario

        return super().save()


