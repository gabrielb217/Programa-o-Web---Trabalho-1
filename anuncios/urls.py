from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('carros/', views.lista_carros, name='lista_carros'),  # Rota para listar os carros
    path('busca/', views.busca_carros, name='busca_carros'),  # Rota para busca
]
