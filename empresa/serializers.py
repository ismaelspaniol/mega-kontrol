from rest_framework import fields
from .models import Empresa
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class EmpresaSerializer(serializers.ModelSerializer):
    data_criacao = fields.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Empresa
        fields = ('id', 'razao_social', 'numero_inscricao', 'data_criacao')
        # fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


