from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anuncios/', views.lista_carros, name='lista_carros'),
    path('cadastrar/', views.criar_carro, name='criar_carro'),
    path('buscar/', views.busca_carros, name='busca_carros'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),  # URL de registro
]
