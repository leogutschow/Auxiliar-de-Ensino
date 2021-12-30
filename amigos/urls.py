from django.urls import path

from amigos.views import MandarSolicitacao

app_name = 'amigo'

urlpatterns = [
    path('adiciona/<int:pk>', MandarSolicitacao.as_view(), name='mandar_solicitacao'),
    # path('remover/<int:pk>', RemoverAmigo.as_view(), name='remover_amigo')
]
