from django.http import JsonResponse
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def listar_pessoas(request):

    if request.method == 'GET':
        pessoa = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoa, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])        
def consultarFuncionario(request, id):
    try:
        pessoa = Pessoa.objects.get(pk=id)
    except Pessoa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
