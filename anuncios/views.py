from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Carro

def home(request):
    return render(request, 'anuncios/home.html')

def lista_carros(request):
    # Obter todos os carros cadastrados
    carros_list = Carro.objects.all()
    # Configurar o paginador para exibir 6 carros por página
    paginator = Paginator(carros_list, 6)
    # Obter o número da página a partir da URL
    page_number = request.GET.get('page')
    # Obter os carros da página atual
    carros = paginator.get_page(page_number)
    # Renderizar o template com os carros paginados
    return render(request, 'anuncios/lista_carros.html', {'carros': carros})

def busca_carros(request):
    query = request.GET.get('q')  # Captura o valor do parâmetro "q" da URL
    if query:
        # Filtra carros com base no modelo ou marca (insensível a maiúsculas/minúsculas)
        carros = Carro.objects.filter(modelo__icontains=query) | Carro.objects.filter(marca__icontains=query)
    else:
        # Exibe todos os carros se não houver busca
        carros = Carro.objects.all()
    return render(request, 'anuncios/lista_carros.html', {'carros': carros})
