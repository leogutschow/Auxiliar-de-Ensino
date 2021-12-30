from django.urls import path, include
from .views import LogOut, PerfilUsuario, SignIn, LogIn

app_name = 'perfil'

urlpatterns = [
    path('login', LogIn.as_view(),name='login'),
    path('logout', LogOut.as_view(), name='logout'),
    path('signin', SignIn.as_view(), name='signin'),
    path('<str:slug>', PerfilUsuario.as_view(), name='perfil_detalhe'),
    
]
