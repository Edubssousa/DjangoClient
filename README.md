# configurações

- python -m django --version -> verifica se o django está instalado
- python -m pip install Django -> instalação do django
- não estamos usando venv!


# comandos
- python manage.py makemigrations -> criação da migração
- python manage.py sqlmigrate polls 0001 -> visualização das tabelas


# o que deve ser feito

<h2> API com comunicação sem erro ou bug das três camadas </h2> 
<ul>
<li> Model -> Class Clients </li> <br>
<li> View -> CRUD </li> <br>
<li> Template -> Django HTML, CSS, <b>FORMS</b> </li> <br>
 </ul>



# o que foi feito

- estou em configurações iniciais
- app Client e urls
- uma view
- criação da model Clients
- criação do arquivo forms
- criação provisória do formulário
- configuração do admin para Clients
- adicão do app Client no settings do ProjetoFinal


# desenvolvimento alisson
- https://docs.djangoproject.com/en/5.0/intro/tutorial02/
- Brincando com a API


# atalhos para produtividade

-  Alt + Seta para cima ->  subir uma linha no VSCode

# no caso de ter o django
- e rodar o comando python -m pip install Django <br>
resultado: <br>
Requirement already satisfied: Django in c:\users\appdata\local\programs\python\python312\lib\site-packages (5.0.6)
Requirement already satisfied: asgiref<4,>=3.7.0 in c:\users\appdata\local\programs\python\python312\lib\site-packages (from Django) (3.8.1)
Requirement already satisfied: sqlparse>=0.3.1 in c:\users\appdata\local\programs\python\python312\lib\site-packages (from Django) (0.5.0)
Requirement already satisfied: tzdata in c:\users\appdata\local\programs\python\python312\lib\site-packages (from Django) (2024.1)
