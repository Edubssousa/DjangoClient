from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse
from .models import Clients
from .serializers import ClientSerializer

# Create your views here.
# talvez precisamos de apenas uma view entregando o CRUD
# pra falar a verdade precimos de apenas duas views



@api_view(['GET'])
def clientsList(request):
    if request.method == 'GET':
        clients = Clients.objects.all()
        serializer = ClientSerializer(clients,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# classe resposável pelo CRUD de um client
@api_view(['GET'])
def ClientCRUD(request):
    if request.method == 'GET':
        return HttpResponse("ClientCRUD")



