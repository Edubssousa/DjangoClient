# VERSÃO BETA COMPLETA E FUNCIONAL


# configurações

- python -m django --version -> verifica se o django está instalado
- python -m pip install Django -> instalação do django
- pip install djangorestframework -> apenas para testes
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

- falta apenas os templates e verificar o forms
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
- criação do CRUD completo com três urls


# desenvolvimento alisson
desenvolvimento completo faltando apenas a integração com os templates
que não foram criados e com os forms, fazendo uma view
sem a necessidade do `rest_framework` para um funcionamento completo


# atalhos para produtividade

-  Alt + Seta para cima ->  subir uma linha no VSCode

# informações importantes

todas as informações estão acima, CRUD COMPLETO E FUNCIONAL
é importante seguir o modelo dos aplicativos django no desenvolvimento
dos templates usando django HTML para possibilitar a integração
das views com os forms com os templates
