from django.contrib import admin
from .models import Prova, Pergunta, Resposta
# Register your models here.


class RespostaInline(admin.StackedInline):
    model = Resposta

class PerguntaInline(admin.TabularInline):
    model = Pergunta
    extras = 0
    can_delete = True
    min_num = 1
    inlines = (RespostaInline,)


class ProvaAdmin(admin.ModelAdmin):
    model = Prova
    inlines = (PerguntaInline,)

admin.site.register(Prova, ProvaAdmin)