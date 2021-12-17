from django.contrib import admin

from especializacao.models import Especializacao

# Register your models here.
class EspecializacaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Especializacao, EspecializacaoAdmin)