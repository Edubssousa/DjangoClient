from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def addClient(request):
    return HttpResponse("adicionar cliente")


def listClients(request):
    return HttpResponse("listar clientes")


def detailsClient(request):
    return HttpResponse("lista de clientes")


def updateClient(request):
    return HttpResponse("Atualizar cliente")


def deleteClient(request):
    return HttpResponse("deletar cliente")
