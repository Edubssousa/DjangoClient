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
@api_view(['GET', 'POST', 'PUT','DELETE'])
def ClientCRUD(request,pk):

    # VALIDAÇÃO

    try:
        client = Clients.objects.get(pk=pk)
    except Clients.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #GET

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    
    #POST

#    if request.method == 'POST':
#       new_client = request.data
#        serializer = ClientSerializer(new_client)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(status.HTTP_400_BAD_REQUEST)  


    #PUT

    if request.method == 'PUT':
        serializer = ClientSerializer(client,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



