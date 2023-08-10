from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes')
]