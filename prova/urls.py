from django.urls import path
from .views import ProvaEdit

app_name = 'prova'

urlpatterns = [
    path('edit/<str:slug>', ProvaEdit.as_view(), name='prova_edit')
]
