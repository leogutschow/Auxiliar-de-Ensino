from django.contrib import admin
from .models import Prova
# Register your models here.

class ProvaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prova, ProvaAdmin)