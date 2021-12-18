from django.urls import path
from .views import Index, Provas

app_name = 'dashboard'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('provas', Provas.as_view(), name='categoria')
]
