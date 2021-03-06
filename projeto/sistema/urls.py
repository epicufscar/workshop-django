from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('adicionar', views.adicionar, name="adicionar"),
    path('aluno/<int:id>/remove', views.remover, name="remover"),
    path('aluno/<int:id>/tranca', views.trancar, name="trancar"),
    path('aluno/<int:id>/editar', views.editar, name="editar"),
]