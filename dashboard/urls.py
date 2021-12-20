from django.urls import path
from .views import Index, ProvaDetalhe, Provas

app_name = 'dashboard'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('provas', Provas.as_view(), name='categoria'),
    path('provas/<str:slug>', ProvaDetalhe.as_view(), name='prova_detalhe'),
]
