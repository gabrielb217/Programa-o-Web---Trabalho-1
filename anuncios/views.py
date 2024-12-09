from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Carro, FotoCarro
from .forms import CarroForm, FotoCarroForm, UserRegisterForm
from django.contrib import messages

def home(request):
    return render(request, 'anuncios/home.html')

def lista_carros(request):
    carros_list = Carro.objects.all()
    paginator = Paginator(carros_list, 6)
    page_number = request.GET.get('page')
    carros = paginator.get_page(page_number)
    return render(request, 'anuncios/lista_carros.html', {'carros': carros})

def busca_carros(request):
    query = request.GET.get('q')
    if query:
        carros = Carro.objects.filter(modelo__icontains=query) | Carro.objects.filter(marca__icontains=query)
    else:
        carros = Carro.objects.all()
    return render(request, 'anuncios/lista_carros.html', {'carros': carros})

@login_required
def criar_carro(request):
    if request.method == 'POST':
        carro_form = CarroForm(request.POST, request.FILES)
        imagens = request.FILES.getlist('imagens')  # Coleta múltiplos arquivos enviados no campo "imagens"

        if carro_form.is_valid():
            carro = carro_form.save(commit=False)
            carro.vendedor = request.user
            carro.save()

            # Salva cada imagem no modelo FotoCarro associada ao carro
            for imagem in imagens:
                FotoCarro.objects.create(carro=carro, imagem=imagem)

            return redirect('lista_carros')
    else:
        carro_form = CarroForm()
        fotos_form = FotoCarroForm()

    return render(request, 'anuncios/criar_carro.html', {'carro_form': carro_form, 'fotos_form': fotos_form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
