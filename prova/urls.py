from django.urls import path
from .views import ProvaDeletar, ProvaEdit, ProvaDetalhe, ProvaCriar

app_name = 'prova'

urlpatterns = [
    path('detalhe/<str:slug>', ProvaDetalhe.as_view(), name='prova_detalhe'),
    path('criar', ProvaCriar.as_view(), name='prova_criar'),
    path('edit/<str:slug>', ProvaEdit.as_view(), name='prova_edit'),
    path('deletar/<int:pk>', ProvaDeletar.as_view(), name='prova_deletar')
]
