# configurações

- python -m django --version -> verifica se o django está instalado
- python -m pip install Django -> instalação do django
- pip install djangorestframework
- não estamos usando venv!


# comandos
- python manage.py makemigrations -> criação da migração
- python manage.py sqlmigrate polls 0001 -> visualização das tabelas

# shell interativo

- from Client.models import Clients
- Client.objects.all()


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
- criação da model Clients
- criação do arquivo forms
- criação provisória do formulário
- configuração do admin para Clients
- adicão do app Client no settings do ProjetoFinal
- criação do super root
- criação de views provisórias
- criação das urls provisórias faltando argumentos
- criação do arquivo serializers
- 'rest_framework' adicionado a INSTALLED_APPS de settings
- mudança nas urls deixando apenas duas
- criação de dois métodos gets e o Client crud incompleto


# desenvolvimento alisson
- https://docs.djangoproject.com/pt-br/5.0/intro/tutorial03/
- Escrevendo mais views


# atalhos para produtividade

-  Alt + Seta para cima ->  subir uma linha no VSCode

# informações importantes

estou vendo sobre a questão de testar as rotas e vejo que 
existe uma necessidade de usar algumas coisas que eu não estava usando antes
