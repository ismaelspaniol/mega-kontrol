from .serializers import EmpresaSerializer
from django_filters import rest_framework as filters
from .models import Empresa
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# como usar autenticacao de token
# https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html#step-4-get-your-token-and-use-your-api


class EmpresaList(viewsets.ModelViewSet):
    # get, post, put, delete
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = (IsAuthenticated,)
    # filter_backends = (filters.DjangoFilterBackend,)




