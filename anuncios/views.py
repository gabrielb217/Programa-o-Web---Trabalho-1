from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Carro
from .forms import CarroForm, FotoCarroForm
from django.contrib import messages
from .forms import UserRegisterForm

def home(request):
    """
    View para a página inicial.
    """
    return render(request, 'anuncios/home.html')

def lista_carros(request):
    """
    View para listar os carros cadastrados com paginação.
    """
    carros_list = Carro.objects.all()  # Obter todos os carros cadastrados
    paginator = Paginator(carros_list, 6)  # Configurar o paginador para exibir 6 carros por página
    page_number = request.GET.get('page')  # Obter o número da página a partir da URL
    carros = paginator.get_page(page_number)  # Obter os carros da página atual
    return render(request, 'anuncios/lista_carros.html', {'carros': carros})

def busca_carros(request):
    """
    View para buscar carros com base no modelo ou marca.
    """
    query = request.GET.get('q')  # Captura o valor do parâmetro "q" da URL
    if query:
        # Filtra carros com base no modelo ou marca (insensível a maiúsculas/minúsculas)
        carros = Carro.objects.filter(modelo__icontains=query) | Carro.objects.filter(marca__icontains=query)
    else:
        # Exibe todos os carros se não houver busca
        carros = Carro.objects.all()
    return render(request, 'anuncios/lista_carros.html', {'carros': carros})

@login_required  # Garante que apenas usuários autenticados possam acessar a página
def criar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            carro = form.save(commit=False)  # Não salva ainda no banco
            carro.vendedor = request.user   # Associa o carro ao usuário autenticado
            carro.save()  # Agora salva o carro com o vendedor
            return redirect('lista_carros')  # Redireciona para a lista de carros
    else:
        form = CarroForm()
    return render(request, 'anuncios/criar_carro.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}!')
            return redirect('login')  # Redireciona para a página de login após o registro
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})