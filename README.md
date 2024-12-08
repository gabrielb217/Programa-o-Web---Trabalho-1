# Plataforma de Vendas de Carros

Este projeto é uma aplicação web para cadastro e gerenciamento de anúncios de carros, desenvolvido como parte de um trabalho acadêmico. O objetivo é permitir que usuários possam cadastrar carros para venda, visualizar anúncios e gerenciar as informações por meio de um painel administrativo.

---

## Funcionalidades
- Cadastro de anúncios de carros, incluindo informações como marca, modelo, ano, preço e descrição.
- Upload de fotos dos carros associados aos anúncios.
- Ambiente administrativo protegido com login/senha (Django Admin).
- Banco de dados relacional com tabelas para carros e fotos.

---

## Tecnologias Utilizadas
- **Python 3.13.1**
- **Django 5.1.4**
- **SQLite** (banco de dados relacional para desenvolvimento rápido e fácil)
- **Bootstrap** (para estilização no frontend - em desenvolvimento)

---

## Requisitos
- **Python** 3.8 ou superior instalado no sistema.
- **Pip** (gerenciador de pacotes do Python).

---

## Como Executar

### Passo 1: Clone o Repositório
- Abra o terminal e digite:
  ```
  git clone <URL_DO_REPOSITORIO>
  ```


### Passo 2: Instale as Dependências
- Instale as bibliotecas necessárias:
  ```
  pip install django pillow
  ```

### Passo 3: Configure o Banco de Dados
- Aplique as migrações para configurar o banco de dados:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

### Passo 4: Crie um Superusuário
- Para acessar o ambiente administrativo, crie um superusuário:
  ```
  python manage.py createsuperuser
  ```

### Passo 5: Inicie o Servidor de Desenvolvimento
- Inicie o servidor local para acessar a aplicação:
  ```
  python manage.py runserver
  ```

### Passo 6: Acesse a Aplicação
- Admin: http://127.0.0.1:8000/admin/
- Página Inicial: http://127.0.0.1:8000/

---

## Estrutura do Projeto
venda_carros/
├── anuncios/               # App principal para gerenciar os anúncios
│   ├── migrations/         # Migrações do banco de dados
│   ├── templates/          # Templates HTML para o frontend
│   ├── admin.py            # Configuração do Django Admin
│   ├── models.py           # Modelos para Carro e Foto
│   └── views.py            # Lógica das páginas
├── venda_carros/           # Configuração principal do projeto
│   ├── settings.py         # Configurações gerais
│   └── urls.py             # Configuração de URLs gerais
├── db.sqlite3              # Banco de dados SQLite
├── manage.py               # Gerenciador do projeto
└── README.md               # Documentação


---

## Licença
- Este projeto foi desenvolvido para fins acadêmicos e não possui uma licença de uso comercial.

---

## Autores
- Francisco 
- Gabriel Raimundo Pereira Barroso
- Lucas



