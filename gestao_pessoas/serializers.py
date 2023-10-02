from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'endereco', 'cpf', 'estado_civil']
